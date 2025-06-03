#!/usr/bin/env bash

prompt="rofi -dmenu -i "

# variables
uptime="$(uptime -p | sed -e 's/up //g')"
host=$(cat /proc/sys/kernel/hostname)

# options
shutdown=' Shutdown'
reboot='󰜉 Reboot'
lock=' Lock'
suspend='󰒲 Suspend'
logout='󰍃 Logout'
hibernate='⏾ Hibernate'
yes=' Yes'
no=' No'

option="$lock\n$suspend\n$logout\n$reboot\n$hibernate\n$shutdown"

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
      swaymsg exit
    elif [[ $1 == 'lock' ]]; then
      swaylock -f -F -e -k -c 000000
    fi
  else
    exit 0
  fi
}

select="$(show_options)"

case $select in
$lock)
  execute lock
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
