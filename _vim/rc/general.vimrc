set encoding=utf-8
scriptencoding utf-8

set clipboard+=unnamed
set helplang=ja,en
set shiftround
set infercase
set hidden
set virtualedit=block
set ambiwidth=double
set autoread
set visualbell t_vb=
set nolazyredraw
set report=0
set fileformats=unix,mac,dos
set nobackup
set nowritebackup
set noswapfile

if !filewritable($HOME."/.vim-backup")
  call mkdir($HOME."/.vim-backup", "p")
endif
set backupdir=$HOME/.vim-backup

if !filewritable($HOME."/.vim-swap")
  call mkdir($HOME."/.vim-swap", "p")
endif
set directory=$HOME/.vim-swap

if has('persistent_undo')
    set undodir=~/.vim/undo
    set undofile
endif
