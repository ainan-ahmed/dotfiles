return {
    {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-tree/nvim-web-devicons",
      "MunifTanjim/nui.nvim",
    },
    opts = {
    sources = { "filesystem", "buffers", "git_status", "document_symbols" },
    open_files_do_not_replace_types = { "terminal", "Trouble", "trouble", "qf", "Outline" },
    filesystem = {
      bind_to_cwd = false,
      follow_current_file = { enabled = true, leave_dirs_open = false, },
      use_libuv_file_watcher = true,
      hide_dotfiles = false,

    },
    },
    config = function()
    vim.keymap.set('n','<C-n>', ':Neotree source=filesystem reveal=true position=left toggle=true<CR>') 
    end

}
}
