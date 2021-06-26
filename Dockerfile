FROM nginx
EXPOSE 80
RUN apt-get -y update
RUN apt-get -y install php-fpm
RUN mkdir -p /var/run/php/
RUN php-fpm7.3 -R
COPY www /usr/share/nginx/html/www
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/.htpasswd /etc/nginx/.htpasswd
