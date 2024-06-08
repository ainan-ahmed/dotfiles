from functions import power, toggle_program
from helpers import load_module
from libqtile import bar
from libqtile.config import Screen
from qtile_extras import widget
import options
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import RectDecoration

colorscheme_module_path = f"themes.{options.default_colorscheme}"
colors = load_module(colorscheme_module_path)
widget_defaults = dict(
    font=options.system_font,
    fontsize=13,
    padding=3,
    background=colors.background,
    foreground=colors.foreground,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.TextBox(
                    padding=10,
                    fontsize=15,
                    # margin=5,
                    fmt="󰣇",
                    # fmt="󰕰",
                    font="FontAwesome",
                    mouse_callbacks={
                        "Button1": lazy.spawn(options.rofi_drun),
                    },
                ),
                widget.Spacer(length=5),
                widget.GroupBox(
                    # fontsize=15,
                    borderwidth=4,
                    highlight_method="line",
                    active=colors.active_w,
                    # block_highlight_text_color=colors.groupbox_colors["hl_text"],
                    # highlight_color=colors.urgent_w,
                    inactive=colors.inactive_w,
                    # foreground=colors.groupbox_colors["fg"],
                    background=colors.groupbox_background,
                    this_current_screen_border=colors.color_w_groupBox,
                    this_screen_border=colors.color_w_groupBox,
                    other_current_screen_border=colors.color_w_groupBox,
                    other_screen_border=colors.color_w_groupBox,
                    urgent_border=colors.urgent_w,
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(length=5),
                widget.CurrentLayoutIcon(use_mask=True, scale=0.8),
                widget.CurrentLayout(
                    fontSize=15,
                ),
                widget.Spacer(length=5),
                widget.Sep(size_percent=70),
                widget.Spacer(length=5),
                widget.WindowName(format="{class}"),
                widget.Spacer(),
                widget.Clock(
                    format="%d.%m.%Y %a %I:%M %p",
                    fontSize=15,
                ),
                widget.Spacer(),
                widget.Systray(
                    decorations=[
                        RectDecoration(
                            colour=colors.foreground,
                            line_colour=colors.foreground,
                            radius=5,
                            # filled=True,
                            group=True,
                            # use_widget_background=True,
                        )
                    ],
                ),
                widget.Spacer(length=-5),
                widget.TextBox(
                    # foreground=colors.foreground,
                    # background=colors.background,
                    padding=15,
                    fontsize=15,
                    margin=3,
                    fmt="",
                    # fmt="󰕰",
                    font="FontAwesome",
                    mouse_callbacks={
                        "Button1": power,
                    },
                ),
            ],
            size=25,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=colors.background,
            background=colors.background,
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
