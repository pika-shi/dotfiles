filetype off
filetype plugin indent off

if has('vim_starting')
      set runtimepath+=~/.vim/bundle/neobundle.vim
endif

let s:neobundle_dir = expand('~/.vim/bundle/')
call neobundle#rc(s:neobundle_dir)

" originalrepos on github
NeoBundleFetch 'Shougo/neobundle.vim'

NeoBundle 'Shougo/vimproc', {
  \ 'build': {
  \   'mac'   : 'make -f make_mac.mak',
  \   'unix'  : 'make -f make_unix.mak',
  \ }}

NeoBundle 'Shougo/unite.vim'
NeoBundle 'Shougo/neomru.vim'
NeoBundle 'Shougo/vimfiler.vim'
NeoBundle 'Shougo/neosnippet'
NeoBundle 'Shougo/neosnippet-snippets'
NeoBundle 'thinca/vim-quickrun'
NeoBundle 'sudar/vim-arduino-syntax'
NeoBundle 'tomtom/tcomment_vim'
NeoBundle 'scrooloose/syntastic'
NeoBundle 'w0ng/vim-hybrid'
NeoBundle 'derekwyatt/vim-scala'
NeoBundle 'pangloss/vim-javascript'
NeoBundle 'mxw/vim-jsx'
NeoBundle 'mattn/emmet-vim'
NeoBundle 'surround.vim'
NeoBundle 'IN3D/vim-raml'


NeoBundle "Shougo/neocomplete.vim"
  let g:neocomplete#enable_at_startup = 1
  let g:neocomplete#enable_ignore_case = 1
  let g:neocomplete#enable_smart_case = 1
  let g:neocomplete#enable_auto_select = 1
  let g:neocomplete#enable_enable_camel_case_completion = 0
  if !exists('g:neocomplete#keyword_patterns')
    let g:neocomplete#keyword_patterns = {}
  endif
  let g:neocomplete#keyword_patterns._ = '\h\w*'
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"

"" unite.vim
let g:unite_enable_start_insert=1
let g:unite_source_history_yank_enable =1

nnoremap <silent> ,uu :<C-u>Unite file_mru buffer<CR>
nnoremap <silent> ,uf :<C-u>UniteWithBufferDir -buffer-name=files file<CR>

au FileType unite nnoremap <silent> <buffer> <expr> <C-J> unite#do_action('split')
au FileType unite inoremap <silent> <buffer> <expr> <C-J> unite#do_action('split')
au FileType unite nnoremap <silent> <buffer> <ESC><ESC> :q<CR>
au FileType unite inoremap <silent> <buffer> <ESC><ESC> <ESC>:q<CR>

"" vimfiler.vim
nnoremap <silent> ,vf :<C-u>VimFiler -split -simple -winwidth=35 -no-quit<CR>

"" syntastic
let g:syntastic_python_checkers = ['flake8', 'pylint']

filetype plugin indent on
set background=dark
colorscheme hybrid
syntax on

" Installation check
NeoBundleCheck
