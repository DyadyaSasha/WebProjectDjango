sudo ln -sf /home/user/WEB_project_nginx/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c ../etc/hello.py hello:app
sudo gunicorn -c ../etc/django_conf.py ask.wsgi

