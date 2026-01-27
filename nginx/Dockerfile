FROM nginx:alpine

# Nginx 설정 복사
COPY default.conf /etc/nginx/conf.d/default.conf

# dist 폴더는 볼륨으로 마운트됨
WORKDIR /usr/share/nginx/html

EXPOSE 80
