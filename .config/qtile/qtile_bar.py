from functions import power, toggle_program
from helpers import load_module
from libqtile import bar
from libqtile.config import Screen
from qtile_extras import widget
import options
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import RectDecoration
import os
colorscheme_module_path = f"themes.{options.default_colorscheme}"
colors = load_module(colorscheme_module_path)
widget_defaults = dict(
    font=options.system_font,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            widgets=[  # type: ignore
                widget.TextBox(
                    foreground=colors.app_launcher_colors["fg"],
                    # background=colors.app_launcher_colors["bg"],
                    padding=10,
                    fontsize=20,
                    # margin=3,
                    fmt="󰣇",
                    # fmt="󰕰",
                    font="FontAwesome",
                    mouse_callbacks={
                        "Button1": lazy.spawn(options.rofi_drun),
                    },
                ),
                widget.Spacer(length=5),
                widget.GroupBox(fontsize=15,
                                borderwidth=5,
                                highlight_method='block',
                                active=colors.groupbox_colors["fg_active"],
                                block_highlight_text_color=colors.groupbox_colors["hl_text"],
                                highlight_color=colors.groupbox_colors["hl_text"],
                                inactive=colors.groupbox_colors["fg_inactive"],
                                foreground=colors.groupbox_colors["fg"],
                                background=colors.groupbox_colors["bg"],
                                this_current_screen_border=colors.groupbox_colors["bg_focus"],
                                this_screen_border=colors.groupbox_colors["bg"],
                                other_current_screen_border=colors.groupbox_colors["bg"],
                                other_screen_border=colors.groupbox_colors["bg"],
                                urgent_border=colors.groupbox_colors["bg_urgent"],
                                rounded=True,
                                disable_drag=True,),
                widget.Spacer(length=5),
                widget.CurrentLayoutIcon(
                    use_mask=True, foreground=colors.other_colors["fg"], scale=.8),
                widget.CurrentLayout(use_mask=True,
                                     foreground=colors.other_colors["fg"],),
                widget.Spacer(length=5),
                widget.Sep(
                    foreground=colors.other_colors["fg"], size_percent=70),
                widget.Spacer(length=5),
                widget.WindowName(
                    format="{class}", foreground=colors.other_colors["fg"],),
                widget.Spacer(),
                widget.Clock(format="%d.%m.%Y %a %I:%M %p",
                             foreground=colors.other_colors["fg"]),
                widget.Spacer(),
                widget.Volume(font=options.system_font, emoji=False, fontSize=15,
                              get_volume_command=os.path.expanduser(
                                  "~/.config/qtile/scripts/get-volume.sh",
                              ), fmt='Vol: {}', padding=10,
                              mouse_callbacks={
                                  "Button1": toggle_program("pavucontrol")},
                              ),
                widget.Systray(decorations=[
                    RectDecoration(
                        colour=colors.other_colors["fg"],
                        line_colour=colors.other_colors["fg"],
                        radius=5,
                        # filled=True,
                        group=True,
                        # use_widget_background=True,
                    )
                ],),
                widget.Spacer(length=-5),
                widget.TextBox(
                    foreground=colors.app_launcher_colors["fg"],
                    # background=colors.app_launcher_colors["bg"],
                    padding=8,
                    fontsize=18,
                    # margin=3,
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
            border_color=colors.other_colors["bar_bg"],
            background = colors.other_colors["bar_bg"],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
