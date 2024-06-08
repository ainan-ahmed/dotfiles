# ██████╗ ████████╗██╗██╗     ███████╗
# ██╔═══██╗╚══██╔══╝██║██║     ██╔════╝
# ██║   ██║   ██║   ██║██║     █████╗
# ██║▄▄ ██║   ██║   ██║██║     ██╔══╝
# ╚██████╔╝   ██║   ██║███████╗███████╗
# ╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝

# ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝
# ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
# ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
# ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
# ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝


import os
import subprocess
import options
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from helpers import load_module
from qtile_bar import screens, widget_defaults
from layouts import layouts, floating_layout
# from libqtile.utils import guess_terminal

#############################################

############## VARIABLES ####################

#############################################

mod = options.mod  # Super key
mod2 = options.mod2  # Alt key
terminal = options.terminal
web_browser = options.web_browser
file_manager = options.file_manager
notify_cmd = options.notify_cmd
colorscheme_module_path = f"themes.{options.default_colorscheme}"
colors = load_module(colorscheme_module_path)

widget_defaults = widget_defaults
rofi_drun = options.rofi_drun
rofi_power = options.rofi_power
#############################################

############## HOOKS ####################

#############################################


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run(["/usr/bin/dex", "-a"])
    # mybar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
    subprocess.run([script])


# Floating dialogs
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == "dialog"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


#############################################

############## KEYBINDINGS ##################


#############################################
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Switch next window on the same group by pressing mod+ ~
    Key([mod], "grave", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # for monadtall layout
    # Key([mod, "control"], "k", lazy.layout.grow()),
    # Key([mod, "control"], "j", lazy.layout.shrink()),
    ############
    # Uncomment this block depending on Layout. Check docs for supported function for the selected layout.
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Block ends here
    Key(
        [mod, "shift"],
        "n",
        lazy.layout.normalize(),
        desc="Reset all secondary window sizes",
    ),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    # # Toggle between split and unsplit sides of stack.
    # # Split = all windows displayed
    # # Unsplit = 1 window displayed, like Max layout, but still with
    # # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    # open terminal by pressing mod+return
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Back-n-forth groups
    Key(
        [mod], "Tab", lazy.screen.toggle_group(), desc="Move to the last visited group"
    ),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key(
        [mod],
        "i",
        lazy.hide_show_bar("top"),
        desc="Hide top bar",
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.reload_config(),
        lazy.spawn(notify_cmd + ' "Configuration Reloaded!"'),
        desc="Reload the config",
    ),
    Key(
        [mod, "shift"],
        "c",
        lazy.restart(),
        lazy.spawn(notify_cmd + ' "Restarting Qtile..."'),
        desc="Restart Qtile",
    ),
    # Shuts down qtile session. You will be redirected to login screen.
    Key(
        [mod, "shift"],
        "e",
        lazy.shutdown(),
        lazy.spawn(notify_cmd + ' "Exiting Qtile..."'),
        desc="Shutdown Qtile",
    ),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn(rofi_drun), desc="run rofi as dmenu"),
    # Lockscreen
    Key(
        [mod], "period", lazy.spawn(options.lock_screen), desc="Launch the lockscreen."
    ),
    Key(["control", "mod1"], "Delete", lazy.spawn(rofi_power), desc="Shutdown menu"),
    # Volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
        desc="Lower Volume by 10%",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
        desc="Raise volume by 10%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute/Unmute volume",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl --player=spotify,%any play-pause"),
        desc="Play/Pause player",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl --player=spotify,%any next"),
        desc="Skip to next",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl --player=spotify,%any previous"),
        desc="Skip to previous",
    ),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# # Add key bindings to switch VTs in Wayland.
# # We can't check qtile.core.name in default config as it is loaded before qtile is started
# # We therefore defer the check until the key binding is run by using .when(func=...)
# for vt in range(1, 8):
#     keys.append(
#         Key(
#             ["control", "mod1"],
#             f"f{vt}",
#             lazy.core.change_vt(vt).when(
#                 func=lambda: qtile.core.name == "wayland"),
#             desc=f"Switch to VT{vt}",
#         )
#     )


# Drag floating layouts.
# Button1 = left button, Button2 = middle button, Button3 = right button
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#############################################

############## GROUPS #######################

#############################################


groups = [
    Group(name="1", spawn=[web_browser], persist=True),
    Group(name="2"),
    Group(name="3"),
    Group(name="4"),
    Group(name="5"),
    Group(name="6"),
    Group(name="7"),
    Group(name="8"),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


#############################################

######## CONFIGURATION VARIABLES ############

#############################################


extension_defaults = widget_defaults.copy()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = "floating_only"
floats_kept_above = True
cursor_warp = False

# If a window requests to be fullscreen, it is automatically fullscreened.
# Set this to false if you only want windows to be fullscreen if you ask them to be.
auto_fullscreen = True

focus_on_window_activation = "urgent"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
