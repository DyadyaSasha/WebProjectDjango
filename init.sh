sudo ln -sf /home/user/WEB_project_nginx/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/user/WEB_project_nginx/etc/hello.py hello:app
