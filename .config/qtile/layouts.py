from libqtile import layout
from helpers import load_module
from libqtile.config import Match
import options

# type: ignore
colorscheme_module_path = f"themes.{
    getattr(options, 'default_colorscheme', 'gruvbox')}"
theme = load_module(colorscheme_module_path)
colors = theme.colors  # type: ignore
# print(colors.client_colors)
gaps_size = options.gaps_size
#############################################

############## LAYOUTS ######################

#############################################
layout_defaults = dict(
    border_focus=theme.border_focus,  # type: ignore
    border_normal=theme.border_normal,  # type: ignore
)
floating_defaults = dict(
    border_focus=colors["red"],
    border_normal=colors["yellow"],
)

layouts = [
    layout.Bsp(
        **layout_defaults,
        border_width=3,
        margin=gaps_size,
        margin_on_single=0,
        border_on_single=0,
    ),
    layout.Max(**layout_defaults),
    layout.MonadTall(
        **layout_defaults,
        single_border_width=0,
        single_margin=0,
        margin=gaps_size,
        border_width=3,
    ),
    # layout.Columns(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadWide(),
    layout.Spiral(
        **layout_defaults,
        border_width=3,
        margin=gaps_size,
        new_client_position="after_current",
    ),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(**layout_defaults),~~~
]

# The default floating layout to use.
floating_layout = layout.Floating(
    **floating_defaults,
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="Lxappearance"),
        Match(wm_class="Nitrogen"),
        Match(wm_class="Pavucontrol"),
        Match(title="Bitwarden"),
        Match(title="Lightdm-gtk-greeter-settings"),
        #
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="Arandr"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(title="branchdialog"),
        Match(role="pop-up"),
    ],
)
