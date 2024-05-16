return {
  {
    'akinsho/bufferline.nvim',
    event = "VeryLazy",
    version = "*",
    dependencies = 'nvim-tree/nvim-web-devicons',
    config = function ()
       local bufferline = require("bufferline")
       bufferline.setup{}
    end
  }

}
