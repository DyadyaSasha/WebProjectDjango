bind = '0.0.0.0:8080'
workers = 3
user = 'nobody'
accesslog='gunicorn_access.log'
errorlog='gunicorn_error.log'
pidfile='gunicorn_pid'
daemon = True

