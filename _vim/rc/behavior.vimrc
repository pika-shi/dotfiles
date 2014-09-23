set autoindent
set smartindent
set wrap
set softtabstop=2
set shiftwidth=2
set expandtab
set formatoptions-=ro
set tabstop=4
set wrapmargin=0
set textwidth=99
set whichwrap=b,s,h,l,<,>,[,]
set backspace=indent,eol,start
set nostartofline
set wildmenu
set wildmode=list:longest,full
set completeopt=menu,menuone
set nrformats=
set history=100
set ignorecase
set smartcase
set wrapscan
set incsearch
set hlsearch

augroup Search
    autocmd!
    autocmd QuickFixCmdPost *grep cwindow
augroup END

au BufNewFile *.html 0r ~/.vim/templates/tmp.html
au BufNewFile *.py 0r ~/.vim/templates/tmp.py

augroup FileTypePlugin
    au!
    au FileType css        setlocal ts=2 sts=2 sw=2
    au FileType scss       setlocal ts=2 sts=2 sw=2
    au FileType html       setlocal ts=2 sts=2 sw=2
    au FileType javascript setlocal ts=2 sts=2 sw=2
    au FileType typescript setlocal ts=2 sts=2 sw=2
    au FileType markdown   setlocal ts=2 sts=2 sw=2 tw=0
    au FileType python     setlocal ts=2 sts=2 sw=2 si cinw=if,elif,else,for,while,try,except,finally,def,class
    au FileType java       setlocal ts=4 sts=4 sw=4
    au FileType vim        setlocal ts=2 sts=2 sw=2
    au FileType vimfiler   setlocal nonu
    au FileType vimshell   setlocal nonu
    au FileType zsh        setlocal ts=2 sts=2 sw=2
augroup END

augroup FileTypeDetect
    au!
    au BufRead,BufNewFile *.json                set filetype=javascript
    au BufRead,BufNewFile *.md                  set filetype=markdown
    au BufRead,BufNewFile .tmux.conf,tmux.conf  set filetype=tmux
    au BufRead,BufNewFile *.jade                set filetype=jade
    au BufRead,BufNewFile *.less                set filetype=less
    au BufRead,BufNewFile *.coffee              set filetype=coffee
    au BufRead,BufNewFile *.scss                set filetype=scss
    au BufRead,BufNewFile *.ts                  set filetype=typescript
augroup END
