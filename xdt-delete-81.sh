#!/bin/bash

xdotool selectwindow

for i in {1..81}
do
    xdotool key ctrl+Delete
    sleep 0.01
    xdotool key Right
    sleep 0.01
done
