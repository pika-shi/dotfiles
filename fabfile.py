# -*- encoding:utf-8 -*-

from fabric.api import env, settings
from fabric.decorators import task, parallel
from fabric.contrib.files import exists
from cuisine import mode_sudo, select_package, run, sudo, package_ensure, dir_exists, cd

env.warn_only = True
env.use_ssh_config = True

@task(default=True)
def main():
    install_packages()
    fetch_dotfiles()
    set_symlinks()
    install_go()
    install_pip()


@task(alias='pkg')
@parallel
def install_packages():
    if exists('/etc/lsb-release'):
        package = 'apt'  # Ubuntu
    elif exists('/etc/redhat-release'):
        package = 'yum'  # RedHat

    select_package(package)

    with settings(mode_sudo()):
        run('{} -y update'.format(package))
        packages = '''
            ag jq tig dfc zsh git tree tmux unzip nodejs golang
            source-highlight silversearcher-ag
        '''.split()
	map(lambda _: package_ensure(_), packages)


@task(alias='go')
@parallel
def install_go():
    if not dir_exists('/usr/local/go'):
        run('wget https://go.googlecode.com/files/go1.2rc2.linux-amd64.tar.gz')
        with settings(mode_sudo()):
            run('tar zxvf go1.2rc2.linux-amd64.tar.gz -C /usr/local')
            run('export PATH=$PATH:/usr/local/go/bin')
            run('go get github.com/peco/peco/cmd/peco')
            run('go get github.com/motemen/ghq')


@task
@parallel
def install_pip():
    run('wget https://bootstrap.pypa.io/get-pip.py')
    with settings(mode_sudo()):
        run('python get-pip.py')
        run('rm get-pip.py')
        run('pip install ipython')
        run('pip install Pygments')

@task
@parallel
def fetch_dotfiles():
    if not dir_exists('dotfiles'):
        run('git clone --recursive https://github.com/pika-shi/dotfiles.git')


@task
@parallel
def set_symlinks():
    with cd('~/'):
        dotfiles = '''
            zshrc zshenv tmux.conf vimrc vim gitignore gitconfig gitattributes
        '''.split()

    if run('uname') == 'Darwin':
        dotfiles += '''zshrc.osx vimparatorrc'''.split()

    for dotfile in dotfiles:
        run('ln -sf dotfiles/_{0} .{0}'.format(dotfile))
