filetype off
filetype plugin indent off

if has('vim_starting')
      set runtimepath+=~/.vim/bundle/neobundle.vim
endif
let s:neobundle_dir = expand('~/.vim/bundle/')
call neobundle#rc(s:neobundle_dir)

" originalrepos on github
NeoBundleFetch 'Shougo/neobundle.vim'

NeoBundle "Shougo/vimproc", { "build": {
  \   "mac"   : "make -f make_mac.mak",
  \   "unix"  : "make -f make_unix.mak",
  \ }}

NeoBundle 'VimClojure'
NeoBundle 'Shougo/vimshell'
NeoBundle 'Shougo/unite.vim'
NeoBundle 'Shougo/vimfiler.vim'
NeoBundle 'Shougo/vimshell.vim'
NeoBundle 'Shougo/neosnippet'
NeoBundle 'Shougo/neosnippet-snippets'
NeoBundle 'jpalardy/vim-slime'
NeoBundle 'scrooloose/syntastic'
NeoBundle "sudar/vim-arduino-syntax"
NeoBundle "thinca/vim-quickrun"

""NeoBundle has('lua') ? 'Shougo/neocomplete' : 'Shougo/neocomplcache'
if neobundle#is_installed('neocomplete')
    " neocomplete用設定
    let g:neocomplete#enable_at_startup = 1
    let g:neocomplete#enable_ignore_case = 1
    let g:neocomplete#enable_smart_case = 1
    if !exists('g:neocomplete#keyword_patterns')
        let g:neocomplete#keyword_patterns = {}
    endif
    let g:neocomplete#keyword_patterns._ = '\h\w*'
elseif neobundle#is_installed('neocomplcache')
    " neocomplcache用設定
    let g:neocomplcache_enable_at_startup = 1
    let g:neocomplcache_enable_ignore_case = 1
    let g:neocomplcache_enable_smart_case = 1
    if !exists('g:neocomplcache_keyword_patterns')
        let g:neocomplcache_keyword_patterns = {}
    endif
    let g:neocomplcache_keyword_patterns._ = '\h\w*'
    let g:neocomplcache_enable_camel_case_completion = 1
    let g:neocomplcache_enable_underbar_completion = 1
endif

if has('python')
    NeoBundleLazy "davidhalter/jedi-vim", {
                \ "autoload": {
                \   "filetypes": ["python", "python3"],
                \ },
                \ "build": {
                \   "mac": "pip install jedi",
                \   "unix": "pip install jedi",
                \ }}
    let s:hooks = neobundle#get_hooks("jedi-vim")
    function! s:hooks.on_source(bundle)
        let g:jedi#auto_vim_configuration = 0
        let g:jedi#popup_select_first = 0
        let g:jedi#rename_command = '<Leader>R'
        let g:jedi#goto_assignments_command = '<Leader>G'
   endfunction
endif

filetype plugin indent on
syntax on

" Installation check
NeoBundleCheck
