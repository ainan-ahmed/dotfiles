"set nocompatible
"call plug#begin()
""Plug 'preservim/nerdtree'
""Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
""Plug 'ctrlpvim/ctrlp.vim'
""Plug 'jiangmiao/auto-pairs'
""Plug 'ellisonleao/gruvbox.nvim'
""Plug 'vim-airline/vim-airline'
""Plug 'ryanoasis/vim-devicons'
""Plug 'fladson/vim-kitty'
""Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
"call plug#end()
"
"
"
"
"
"
"
"
"
"
"set termguicolors
"colorscheme catppuccin-mocha
"set background=dark
""compile and run
"autocmd filetype cpp nnoremap <F5> :w <bar> !g++ -ulimit -Wall -Wno-unused-result -std=c++17   -O2   % -o %:r && ./%:r < ./input.txt<CR>
"autocmd filetype cpp nnoremap <F6> :w <bar> !g++ -ulimit -Wall -Wno-unused-result -std=c++17   -O2   % -o %:r && ./%:r <CR>
""
"
"
"
""sets line numbering
"set number
"
"syntax enable
""Hightlights current line
"set cursorline
""removes the underline causes by enabling cursorline
"hi clear CursorLine
"
"set smarttab
"set tabstop=4
"set softtabstop=4
"set shiftwidth=4
"set textwidth=79
"
"set autoindent
"set smartindent
"set splitright
"set splitbelow
"set hlsearch
"set incsearch
"set showmatch
"set wildmenu
"set foldenable
"set foldlevelstart=99
"set foldmethod=indent
"nnoremap <space> za
"
"
"set encoding=utf-8
"set mouse=a
"map <C-n> :NERDTreeToggle<CR>
