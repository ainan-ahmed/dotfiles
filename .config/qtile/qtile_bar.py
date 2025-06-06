from libqtile import bar
from libqtile.config import Screen
from qtile_extras import widget
from libqtile.lazy import lazy
from functions import power
from helpers import load_module
import options


colorscheme_module_path = f"themes.{getattr(options, 'default_colorscheme', 'gruvbox')}"
theme = load_module(colorscheme_module_path)
# print(theme)
colors = theme.colors  # type: ignore
widget_defaults = dict(
    font=options.system_font,
    fontsize=13,
    padding=3,
    background=colors["bg"],
    foreground=colors["red"],
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
                    active=colors["red"],
                    # block_highlight_text_color=colors["fg"],
                    highlight_color=colors["bg"],
                    inactive=colors["fg_gutter"],
                    foreground=colors["red"],
                    background=colors["bg"],
                    this_current_screen_border=colors["red"],
                    this_screen_border=colors["red"],
                    other_current_screen_border=colors["magenta"],
                    # other_screen_border=colors["magenta"],
                    urgent_border=colors["yellow"],
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
                    foreground=colors["red"],
                    background=colors["bg"],
                ),
                widget.Spacer(),
                widget.UPowerWidget(),
                widget.ALSAWidget(
                    mode="popup",
                    limit_loud=100,
                    popup_hide_timeout=2,
                    update_interval=1,
                ),
                #  widget.BrightnessControl(
                #       mode="popup",
                #   ),
                widget.Systray(
                    background=colors["bg"], icon_size=16, foreground=colors["red"]
                ),
                widget.Spacer(length=-5),
                widget.TextBox(
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
            border_color=colors["red"],
            background=colors["bg"],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
