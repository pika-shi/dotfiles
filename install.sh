#!/bin/sh

# install and bundle homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew bundle

# install easy_install
# wget https://bootstrap.pypa.io/ez_setup.py
# sudo python ez_setup.py
# rm ez_setup.py
#
# # install fabric cuisine
# sudo easy_install fabric cuisine
#
# # run fabfile
# fab main --initial-password-prompt -H localhost
