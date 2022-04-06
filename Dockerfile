FROM nginx
EXPOSE 80
COPY www /usr/share/nginx/html/www
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/.htpasswd /etc/nginx/.htpasswd
COPY conf/cmd.sh /start.sh
CMD [ "/start.sh" ]
