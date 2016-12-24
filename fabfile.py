# -*- encoding:utf-8 -*-

from fabric.api import env, shell_env, settings
from fabric.decorators import task, parallel
from fabric.contrib.files import exists, console
from fabric.colors import white
from cuisine import mode_sudo, select_package, run, sudo, package_ensure, dir_exists, file_exists, cd

env.warn_only = True
env.use_ssh_config = True
#env.key_filename = '~/.ssh/id_rsa'

@task(default=True)
@parallel
def main():
    install_linux_packages()
    install_ruby_packages()
    install_go_packages()
    install_python27()
    install_python_packages()
    install_diff_highlight()
    clone_dotfiles()
    clone_tpm()
    generate_sshkey()
    set_symlinks()
    #change_shell()


@task
@parallel
def setup_mac():
    dotfiles_path = '~/.ghq/github.com/pika-shi/dotfiles'
    clone_dotfiles(dotfiles_path)
    set_symlinks(dotfiles_path)
    restore_mackup()
    clone_tpm()
    change_shell()
    set_mac_environment()


@task(alias='pkg')
@parallel
def install_linux_packages():
    print white('--- install linux packages ---', bold=True)
    if exists('/etc/lsb-release'):
        manager = 'apt'  # Ubuntu
        packages = '''
            jq tig dfc zsh git tree tmux unzip nodejs golang
            source-highlight silversearcher-ag vim zlib1g-dev libssl-dev
            python-software-properties software-properties-common
        '''.split()
    elif exists('/etc/redhat-release'):
        manager = 'yum'  # RedHat
        packages = '''
            jq tig dfc zsh git tree tmux unzip nodejs golang
            source-highlight vim zlib-devel openssl-devel
        '''.split()
    select_package(manager)
    with settings(mode_sudo()):
        run('{} -y update'.format(manager))
	map(lambda _: package_ensure(_), packages)
        if exists('/etc/lsb-release'):  # tmux 2.0
            run('add-apt-repository -y ppa:pi-rho/dev')
            run('apt-get update')
            run('apt-get install -y tmux=2.0-1~ppa1~t')


@task(alias='ruby')
@parallel
def install_ruby_packages():
    print white('--- install ruby packages ---', bold=True)
    with settings(mode_sudo()):
        run('gem install tmuxinator')


@task(alias='go')
@parallel
def install_go_packages():
    print white('--- install go packages ---', bold=True)
    with shell_env(GOPATH='/home/{}/.go'.format(run('whoami'))):
        run('go get github.com/peco/peco/cmd/peco')
        run('go get github.com/motemen/ghq')


@task(alias='python')
@parallel
def install_python27():
    print white('--- install python2.7 ---', bold=True)
    #if not file_exists('/usr/local/bin/python2.7'):
    with cd('~/'):
        run('curl -O https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz')
        run('tar zxvf Python-2.7.9.tgz')
    with cd('/home/{}/Python-2.7.9'.format(run('whoami'))):
        run('./configure')
        run('make')
        sudo('make install')
    with cd('~/'):
        run('rm Python-2.7.9.tgz')
        run('rm -rf Python-2.7.9')


@task(alias='pip')
@parallel
def install_python_packages():
    print white('--- install python packages ---', bold=True)
    if not file_exists('/usr/bin/pip'):
        run('wget https://bootstrap.pypa.io/get-pip.py')
        with settings(mode_sudo()):
            run('/usr/local/bin/python2.7 get-pip.py')
            run('rm get-pip.py')
        with settings(mode_sudo()):
            run('ln -sf /usr/local/bin/pip /usr/bin/pip')
            run('pip install ipython')
            run('pip install virtualenv')
            run('pip install Pygments')


@task
@parallel
def install_diff_highlight():
    print white('--- install diff highlight ---', bold=True)
    if not file_exists('/usr/local/bin/diff-highlight'):
        run('wget https://raw.githubusercontent.com/git/git/master/contrib/diff-highlight/diff-highlight')
        with settings(mode_sudo()):
            run('chmod +x diff-highlight')
            run('mv diff-highlight /usr/local/bin/diff-highlight')


@task
@parallel
def clone_dotfiles(dest='.'):
    print white('--- clone dotfiles ---', bold=True)
    if not dir_exists('dotfiles') and console.confirm('Set sshkey to github?'):
        run('git clone --recursive https://github.com/pika-shi/dotfiles.git {0}'.format(dest))


@task
@parallel
def clone_tpm():
    print white('--- clone tpm ---', bold=True)
    if not dir_exists('.tmux'):
        run('git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm')


@task
def set_symlinks(src='dotfiles'):
    print white('--- set symlinks ---', bold=True)
    with cd('~/'):
        dotfiles = '''
            zshrc zshenv tmux.conf vimrc vim gitignore gitconfig gitattributes mackup.cfg
        '''.split()
        map(lambda _: run('ln -sf {0}/_{1} .{1}'.format(src, _)), dotfiles)


@task
def change_shell():
    print white('--- change shell ---', bold=True)
    run('chsh -s /usr/local/bin/zsh')


@task
def restore_mackup():
    print white('--- restore mackup ---', bold=True)
    run('mackup restore')

@task
def set_mac_environment():
    print white('--- set mac environment ---', bold=True)
    sudo('nvram SystemAudioVolume=%80')

    run('defaults write com.apple.dock autohide -bool true')
    run('defaults write com.apple.dock autohide-delay -float 0')
    run('defaults write com.apple.dock magnification -bool true')
    run('defaults write com.apple.dock tilesize -int 40')
    run('defaults write com.apple.dock largesize -int 80')
    run('defaults write com.apple.dock mineffect -string "scale"')
    run('killall Dock')

    run('defaults write com.apple.finder CreateDesktop -bool false')
    run('killall Finder')
