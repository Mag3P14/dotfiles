#!/bin/bash
scrot -b -d 5 '%Y:%m:%d:%H:%M:%S.png' -e 'mv $f ~/Pictures/Screenshots/'
