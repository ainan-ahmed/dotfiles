local opt = vim.opt
local g = vim.g

opt.expandtab = true -- Use spaces instead of tabs
opt.tabstop = 2
opt.softtabstop = 2
opt.shiftwidth = 2
opt.number = true
opt.confirm = true -- Confirm to save changes before exiting modified buffer
--vim.cmd("set cursorline")
opt.cursorline = true
opt.splitright = true
opt.splitbelow = true
opt.foldlevel = 99
opt.foldmethod = "indent"
opt.termguicolors = true
opt.showmode = false -- Dont show mode since we have a statusline
g.clipboard = "CopyQ" -- Sync wit system clipboard
g.smoothscroll = true
g.mapleader = " "
g.autoformat = true
g.autochdir = true
