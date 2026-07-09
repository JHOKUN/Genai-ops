FROM alpine:latest

RUN apk add --no-cache apache2

EXPOSE 80

ENTRYPOINT /usr/sbin/httpd -DFOREGROUND


FROM alpine:latest
RUN apk add --no-cache git
RUN apk add --no-cache mysql-client