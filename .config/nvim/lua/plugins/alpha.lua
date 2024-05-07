return{
    'goolord/alpha-nvim',
    config = function ()
        local alpha = require("alpha")
        local dashboard = require("alpha.themes.dashboard")
        -- Set header
        dashboard.section.header.val = {
        "                                                                                          ",
        "                   ███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗                     ",
        "                   ████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║                     ",
        "                   ██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║                     ",
        "                   ██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║                     ",
        "                   ██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║                     ",
        "                   ╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝                     ",
        "                                                                                          ",
        "    ------------------------------------------------------------------------------        ",
"                                                                                                  ",
        "  ██╗  ██╗███████╗██╗     ██╗      ██████╗      █████╗ ██╗███╗   ██╗ █████╗ ███╗   ██╗██╗ ",
        "  ██║  ██║██╔════╝██║     ██║     ██╔═══██╗    ██╔══██╗██║████╗  ██║██╔══██╗████╗  ██║██║ ",
        "  ███████║█████╗  ██║     ██║     ██║   ██║    ███████║██║██╔██╗ ██║███████║██╔██╗ ██║██║ ",
        "  ██╔══██║██╔══╝  ██║     ██║     ██║   ██║    ██╔══██║██║██║╚██╗██║██╔══██║██║╚██╗██║╚═╝ ",
        "  ██║  ██║███████╗███████╗███████╗╚██████╔╝    ██║  ██║██║██║ ╚████║██║  ██║██║ ╚████║██╗ ",
        "  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ",


        }
        -- Set menu
        dashboard.section.buttons.val = {
            dashboard.button("f", "   Find file", ":Telescope find_files<CR>"),
            dashboard.button("p", "   Projects", ":Telescope projects<CR>"),
            dashboard.button("r", "   Recent", ":Telescope oldfiles<CR>"),
            dashboard.button("l", " 󰒲 " .. " Lazy", "<cmd> Lazy <cr>"),
            dashboard.button("m", "  " .. " Mason", "<cmd> Mason <cr>"),
            dashboard.button("q", "   Quit NVIM", ":qa<CR>"),
        }

        alpha.setup(dashboard.opts)
    end
};