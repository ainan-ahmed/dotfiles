#!/bin/bash

bluetoothctl
sleep 5
echo "connect B0:73:9C:33:E4:7F" | bluetoothctl
sleep 10
echo "connect B0:73:9C:33:E4:7F" | bluetoothctl
exit
