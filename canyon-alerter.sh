#!/bin/bash


./alert.py 2369 SR/BK M || ./telegram.sh "Grail 6 Silver M is available!"
./alert.py 2369 GN/BK M || ./telegram.sh "Grail 6 Matcha M is available!"
#./alert.py 2370 SR/BK M || ./telegram.sh "Grail 7 Silver M is available!"
#./alert.py 2370 GN/BK M || ./telegram.sh "Grail 7 Matcha M is available!"
