#!/bin/sh
./webXiv_bot.py &
php-fpm7.3 -R; nginx
/bin/bash