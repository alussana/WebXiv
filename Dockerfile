FROM nginx
COPY www /usr/share/nginx/html/www
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/.htpasswd /etc/nginx/.htpasswd
EXPOSE 80
