#!/bin/sh
python dataserver.py&
sudo lxterminal -e python3 combine.py&
sudo lxterminal -e python cameraCodeVideo.py&
wait