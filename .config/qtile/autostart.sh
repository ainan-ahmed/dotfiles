#!/bin/bash

# Monitor Configuaration script
#sh ~/.screenlayout/monitorLayout.sh &
# Picom compositor
picom --config ~/.config/picom/picom.conf -b &
# Notification Deamon
dunst --config ~/.config/dunst/dunstrc &
# Background wallpaper setter
nitrogen --restore &
# Enable Numlock on startup
xdotool key --clearmodifier Num_Lock &
# Network manager applet
nm-applet &
# Bluetooth applet
blueman-applet &
# Volume control applet
pasystray &
# Bluelight filter
redshift-gtk &

