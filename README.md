

### install depndencies ###

$ sudo pip install -r requirements.txt

$ python3 manage.py run

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/
    
###USE THE FOLLOWING COMMAND TO RUN USING GUNICORN-WSGI ON THE PRODUCTION SERVER(ONLY LINUX) ###


$ sudo nohup gunicorn --config ./gunicorn_config.py wsgi:app &


