# -*- encoding:utf-8 -*-

from fabric.api import env, local, lcd
from fabric.decorators import task
from fabric.contrib import console
from fabric.colors import white


env.warn_only = True
dotfiles_path = '.ghq/github.com/pika-shi/dotfiles'


@task(default=True)
def main():
    clone_dotfiles()
    set_symlinks()
    restore_mackup()
    change_shell()
    set_mac_environment()


@task
def clone_dotfiles():
    print white('--- clone dotfiles ---', bold=True)
    with lcd('~/'):
        if console.confirm('Set sshkey to github?'):
            local('git clone --recursive git@github.com:pika-shi/dotfiles.git {0}'.format(dotfiles_path))


@task
def set_symlinks():
    print white('--- set symlinks ---', bold=True)
    with lcd('~/'):
        dotfiles = '''
	    zshrc zshenv tmux.conf vimrc tmux vim gitignore gitconfig gitattributes mackup.cfg
        '''.split()
        map(lambda _: local('ln -sf {0}/_{1} .{1}'.format(dotfiles_path, _)), dotfiles)


@task
def change_shell():
    print white('--- change shell ---', bold=True)
    local('echo "/usr/local/bin/zsh" | sudo tee -a /etc/shells')
    local('chsh -s /usr/local/bin/zsh')


@task
def restore_mackup():
    print white('--- restore mackup ---', bold=True)
    local('mackup restore')


@task
def set_mac_environment():
    print white('--- set mac environment ---', bold=True)
    local('nvram SystemAudioVolume=%80')

    local('defaults write com.apple.dock autohide -bool true')
    local('defaults write com.apple.dock autohide-delay -float 0')
    local('defaults write com.apple.dock magnification -bool true')
    local('defaults write com.apple.dock tilesize -int 40')
    local('defaults write com.apple.dock largesize -int 80')
    local('defaults write com.apple.dock mineffect -string "scale"')
    local('killall Dock')

    local('defaults write com.apple.finder CreateDesktop -bool false')
    local('killall Finder')
