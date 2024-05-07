from libqtile import layout
from helpers import load_module
from libqtile.config import Match
import options
colorscheme_module_path = f"themes.{options.default_colorscheme}"
colors = load_module(colorscheme_module_path)
# print(colors.client_colors)
gaps_size = options.gaps_size
#############################################

############## LAYOUTS ######################

#############################################


layouts = [
    layout.MonadTall(single_border_width=0, single_margin=0, border_normal=colors.client_colors["border"],
                     border_focus=colors.client_colors["border_focus"], margin=gaps_size, border_width=3,),
    # layout.Columns(),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),

    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

# The default floating layout to use.
floating_layout = layout.Floating(
    border_focus=colors.client_colors["border_floating"],
    border_normal=colors.client_colors["border"],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="Lxappearance"),
        Match(wm_class="Nitrogen"),
        Match(wm_class="Pavucontrol"),
        Match(title='Bitwarden'),
        #
        Match(wm_class='confirm'),
     Match(wm_class='dialog'),
     Match(wm_class='download'),
     Match(wm_class='error'),
     Match(wm_class='file_progress'),
     Match(wm_class='notification'),
     Match(wm_class='splash'),
     Match(wm_class='toolbar'),
     Match(wm_class='confirmreset'),
     Match(wm_class='makebranch'),
     Match(wm_class='maketag'),
     Match(title='branchdialog'),
        Match(title='pop-up'),
    ]
)
