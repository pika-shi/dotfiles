syntax on

set listchars=tab:▸\ ,eol:¬
set list
set showcmd                 " display incomplete commands
set number                  " line numbers
set cmdheight=1             " command line height
set shortmess=altoO         " shorten messages
set scrolloff=5             " Keep at least 5 lines above and below the cursor
set laststatus=2            " The last window always have status line
set showmatch               " brackets/braces that is
set matchtime=3             " duration to show matching brace (1/10 sec)
set ruler                   " show the cursor position all the time
set foldmethod=marker
execute "set colorcolumn=" . join(range(81, 9999), ',')
set colorcolumn+=1

if has("mouse") " Enable the use of the mouse in all modes
  set mouse=a
endif

" highlight cursor line in current window
augroup cch
    autocmd!
    autocmd WinLeave * set nocursorline
    autocmd WinEnter,BufRead * set cursorline
augroup END
highlight clear CursorLine
highlight CursorLine ctermbg=black
