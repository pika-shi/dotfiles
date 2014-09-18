# -*- encoding:utf-8 -*-

from fabric.api import env, settings
from fabric.decorators import task
from cuisine import mode_sudo, select_package, run, package_ensure, dir_exists, cd

env.warn_only = True
env.hosts = ['hoge']
select_package('apt')

@task
def main():
  setup_packages()
  install_go()
  install_pip()
  fetch_dotfiles()
  set_symlinks()
  change_shell()
  complete_brew()

@task
def setup_packages():
  with settings(mode_sudo()):
    run('apt-get update')
    run('apt-get -y upgrade')
    package_ensure('ag')
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
  run('wget https://go.googlecode.com/files/go1.2rc2.linux-amd64.tar.gz')
  with settings(mode_sudo()):
    run('tar zxvf go1.2rc2.linux-amd64.tar.gz -C /usr/local')
    run('export PATH=$PATH:/usr/local/go/bin')
    run('go get github.com/peco/peco/cmd/peco')
    run('go get github.com/motemen/ghq')

@task
def install_pip():
  run('wget https://bootstrap.pypa.io/get-pip.py')
  with setting(mode_sudo()):
    run('python get-pip.py')
    run('rm get-pip.py')
    run('pip install ipython')
    run('pip install Pygments')

@task
def fetch_dotfiles():
  run('wget https://github.com/pika-shi/dotfiles/archive/master.zip')
  if not dir_exists('dotfiles'):
    run('unzip master.zip')
    run('rm master.zip')
    run('mv dotfiles-master dotfiles')

@task
def set_symlinks():
  with cd('dotfiles'):
    path_list = [('_zshrc', '~/.zshrc'),
                 ('_zshenv', '~/.zshenv'),
                 ('_tmux.conf', '~/.tmux.conf'),
                 ('_vimrc', '~/.vimrc'),
                 ('_vim', '~/.vim'),
                 ('_gitignore', '~/.gitignore'),
                 ('_gitconfig', '~/.gitconfig'),
                 ('_gitattributes', '~/.gitattributes')]
  if 'localhost' in env.hosts:
    path_list.append(('_zshrc.osx', '~/.zshrc.osx'))
    path_list.append(('_vimperatorrc', '~/.vimperatorrc'))
    path_list.append(('karabiner.xml',
                      '~/Library/Application Support/Karabiner/private.xml'))
    path_list.append(('/usr/local/Library/Contributions/brew_zsh_completion.zsh',
                      '/usr/local/share/zsh/site-functions/_brew'))

  with cd('~/'):
    for path_set in path_list:
      run('ln -sf %s %s' % (path_set[0], path_set[1]))

@task
def change_shell():
  run('sed -i "s/^\(.*pam_shells.so$\)/#\1/" /etc/pam.d/chsh')
  run('zsh')

@task
def complete_brew():
  with cd('/usr/local/share/zsh/site-functions'):
    run('ln -sf ../../../Library/Contributions/brew_zsh_completion.zsh _brew')
