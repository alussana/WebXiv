#!/bin/sh

# uncomment the following line to enable the messaging telegram bot
# if you do so, see also Dockerfile
#./webXiv_bot.py &
php-fpm7.3 -R; nginx
/bin/bash
