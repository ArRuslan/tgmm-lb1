#!/bin/bash

xdotool selectwindow

for i in {1..117}
do
    xdotool key ctrl+Delete
    sleep 0.05
    xdotool key Right
    sleep 0.05
done
