#!/usr/bin/env bash

prompt="rofi -dmenu -i -theme ~/.config/rofi/scripts/powermenu.rasi"

# variables
uptime="$(uptime -p | sed -e 's/up //g')"
host=$(cat /proc/sys/kernel/hostname)
dwm_pid="$(pidof dwm)"

# options
shutdown=' Shutdown'
reboot='󰜉 Reboot'
lock=' Lock'
suspend='󰒲 Suspend'
logout='󰍃 Logout'
hibernate='⏾ Hibernate'
yes=' Yes'
no=' No'

option="$lock\n$hibernate\n$suspend\n$logout\n$reboot\n$shutdown"

show_options() {
  echo -e "$option" | $prompt -p "$host" -mesg "Uptime: $uptime"
}
confirmation() {
  echo -e "$yes\n$no" | $prompt -p "Confirmation" -mesg "Are you sure?"
}
execute() {
  confirm="$(confirmation)"
  wm="$(wmctrl -m | grep \"Name: \" | awk '{print $2}')"

  if [[ "$confirm" == "$yes" ]]; then
    if [[ $1 == 'shutdown' ]]; then
      systemctl poweroff
    elif [[ $1 == 'hibernate' ]]; then
      systemctl hibernate
    elif [[ $1 == 'reboot' ]]; then
      systemctl reboot
    elif [[ $1 == 'suspend' ]]; then
      systemctl suspend
    elif [[ $1 == 'logout' ]]; then
      if [[ $wm == 'dwm' ]]; then
        kill -TERM dwmpid $dwm_pid
      elif [[ $wm == 'awesome' ]]; then
        awesome-client 'awesome.quit()'
      elif [[ $wm == 'openbox' ]]; then
        openbox --exit
      elif [[ $wm == 'bspwm' ]]; then
        bspc quit
      elif [[ $wm == 'i3' ]]; then
        i3-msg exit
      elif [[ $wm == 'plasma' ]]; then
        qdbus org.kde.ksmserver /KSMServer logout 0 0 0
      elif [[ $wm == 'wlroots' ]]; then
        hyprctl dispatch exit
      elif [[ $wm == 'LG3D' ]]; then
        qtile cmd-obj -o cmd -f shutdown
      fi
    fi
  else
    exit 0
  fi
}

select="$(show_options)"

case $select in
$lock)
  slock
  ;;
$hibernate)
  execute hibernate
  ;;
$suspend)
  execute suspend
  ;;
$logout)
  execute logout
  ;;
$reboot)
  execute reboot
  ;;
$shutdown)
  execute shutdown
  ;;
esac
