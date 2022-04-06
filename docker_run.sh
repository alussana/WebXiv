#!/bin/bash
docker run -it -v /$1:/usr/share/nginx/html/Xiv -p $2:80 webxiv
