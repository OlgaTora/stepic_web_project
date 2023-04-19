#!/bin/bash

sudo ln -sf home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


#sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart

sudo gunicorn --bind 127.0.0.1:8080 hello:wsgi_application


