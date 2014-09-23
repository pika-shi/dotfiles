# -*- encoding:utf-8 -*-

from fabric.api import env, settings
from fabric.decorators import task
from cuisine import mode_sudo, select_package, run, sudo, package_ensure, dir_exists, cd

env.warn_only = True
env.use_ssh_config = True

@task
def main(package='apt', git=0):
  setup_packages(package)
  fetch_dotfiles(git)
  set_symlinks()
  change_shell()
  install_go()
  install_pip()

@task
def setup_packages(package):
  select_package(package)
  with settings(mode_sudo()):
    run('{0} -y update'.format(package))
    run('{0} -y upgrade'.format(package))
    package_ensure('ag')
    package_ensure('jq')
    package_ensure('tig')
    package_ensure('dfc')
    package_ensure('zsh')
    package_ensure('git')
    package_ensure('lftp')
    package_ensure('tree')
    package_ensure('tmux')
    package_ensure('unzip')
    package_ensure('nodejs')
    package_ensure('golang')
    package_ensure('source-highlight')
    package_ensure('silversearcher-ag')

@task
def install_go():
  if not dir_exists('/usr/local/go'):
    run('wget https://go.googlecode.com/files/go1.2rc2.linux-amd64.tar.gz')
    with settings(mode_sudo()):
      run('tar zxvf go1.2rc2.linux-amd64.tar.gz -C /usr/local')
      run('export PATH=$PATH:/usr/local/go/bin')
      run('go get github.com/peco/peco/cmd/peco')
      run('go get github.com/motemen/ghq')

@task
def install_pip():
  run('wget https://bootstrap.pypa.io/get-pip.py')
  with settings(mode_sudo()):
    run('python get-pip.py')
    run('rm get-pip.py')
    run('pip install ipython')
    run('pip install Pygments')

@task
def fetch_dotfiles(git):
  if not dir_exists('dotfiles'):
    if git:
      run('git clone --recursive git@github.com:pika-shi/dotfiles.git')
    else:
      run('wget https://github.com/pika-shi/dotfiles/archive/master.zip')
      run('unzip master.zip')
      run('rm master.zip')
      run('mv dotfiles-master dotfiles')

@task
def set_symlinks():
  with cd('~/'):
    path_list = [('dotfiles/_zshrc', '.zshrc'),
                 ('dotfiles/_zshenv', '.zshenv'),
                 ('dotfiles/_tmux.conf', '.tmux.conf'),
                 ('dotfiles/_vimrc', '.vimrc'),
                 ('dotfiles/_vim', '.vim'),
                 ('dotfiles/_gitignore', '.gitignore'),
                 ('dotfiles/_gitconfig', '.gitconfig'),
                 ('dotfiles/_gitattributes', '.gitattributes')]
    if run('uname') == 'Darwin':
      path_list.append(('dotfiles/_zshrc.osx', '.zshrc.osx'))
      path_list.append(('dotfiles/_vimperatorrc', '.vimperatorrc'))
      path_list.append(('dotfiles/karabiner.xml',
                        'Library/Application Support/Karabiner/private.xml'))
      path_list.append(('/usr/local/Library/Contributions/brew_zsh_completion.zsh',
                        '/usr/local/share/zsh/site-functions/_brew'))

    for path_set in path_list:
      run('ln -sf {0} {1}'.format(path_set[0], path_set[1]))

@task
def change_shell():
    sudo('sed -i "s/^\(.*pam_shells.so$\)/#\1/" /etc/pam.d/chsh')
