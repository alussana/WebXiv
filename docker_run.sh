#!/bin/bash
docker run -it -v /$1:/usr/share/nginx/html/Xiv -v /$2:/usr/share/nginx/html/inbox -p $3:80 webxiv
