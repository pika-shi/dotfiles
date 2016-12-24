#!bin/sh

# install and bundle homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew bundle

# setup python environment and install some libraries
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 2.7.13
pyenv virtualenv 2.7.13 default
pyenv global default
pyenv exec pip install fabric cuisine ipython

# execute fabric script
fab -f fabfile_local.py -H localhost
