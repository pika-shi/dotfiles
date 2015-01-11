syntax on

set listchars=tab:▸\ ,eol:¬
set list
set showcmd
set number
set cmdheight=1
set shortmess=altoO
set scrolloff=5
set laststatus=2
set showmatch
set matchtime=3
set ruler
set foldmethod=marker
set colorcolumn+=81

augroup cch
    autocmd!
    autocmd WinLeave * set nocursorline
    autocmd WinEnter,BufRead * set cursorline
augroup END

augroup whitespace
    autocmd!
    autocmd VimEnter,WinEnter * match WhitespaceEOL /\s\+$/
augroup END
highlight WhitespaceEOL ctermbg=red guibg=red
