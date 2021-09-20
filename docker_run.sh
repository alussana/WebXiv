#!/bin/bash
docker run -it -v /$1:/usr/share/nginx/html/Xiv -v /$2:/usr/share/nginx/html/inbox -p 8088:80 webxiv
