set autoindent
set smartindent
set wrap
set softtabstop=2
set shiftwidth=2
set expandtab
set formatoptions=-ro
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
