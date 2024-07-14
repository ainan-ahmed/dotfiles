#!/bin/bash
bluetoothctl <<EOF
power on
agent on
connect B0:73:9C:33:E4:7F
exit
EOF
