#!/bin/bash
setxkbmap -layout 'cz' -variant 'coder' && pkill -RTMIN+12 i3blocks
xmodmap -e 'keycode 0x42 = Escape'
