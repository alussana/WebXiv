FROM nginx
EXPOSE 80
RUN apt-get -y update
RUN apt-get -y install apt-utils
RUN apt-get -y install php-fpm
RUN apt-get -y install net-tools
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install python-telegram-bot --upgrade
RUN pip3 install requests
RUN pip3 install python-dotenv
RUN mkdir -p /var/run/php/
RUN sed -i "s|listen = /run/php/php7.3-fpm.sock|listen = 127.0.0.1:9000|" /etc/php/7.3/fpm/pool.d/www.conf
COPY www /usr/share/nginx/html/www
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/.htpasswd /etc/nginx/.htpasswd
COPY conf/cmd.sh /start.sh
COPY telegram_bot/* / 
CMD [ "/start.sh" ]
