The are additional configuration files if you are using uWSGI and NGINX for your web server.
If you are using Apache or something else, I haven't used it and unfortinately can't help you with them.


Note: 
In the files below, anyplace that says /home/mon -- replace mon with the user name you are installing this.
In the files below, anyplace that says /home/mon/garage-door -- replace it with the directory you are installing this.
In the files below, anyplace that says /home/mon/garage-door/venv -- replace it with the virtual environment name you are using.


FileName: garage-door.ini
CopyTo: ~/garage-door/garage-door.ini


FileName: garage-door.service
CopyTo: /etc/systemd/system/garage-door.service


FileName: garage-door [note no extension on this one]
CopyTo: /etc/nginx/sites-available/garage-door



If it helps at all, I have been using these sites as info and advice:
digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
nginx.org/en/docs/http/server_names.html
stackoverflow.com/questions/11954255/how-to-set-index-html-as-root-file-in-nginx




Once you have the above files in-place, these commands should get you up and running.
sudo systemctl start garage-door (or whatever you named your .service file)
sudo systemctl enable garage-door
sudo ln -s /etc/nginx/sites-available/garage-door /etc/nginx/sites-enabled (this one just links the sites-enabled to sites-available. Only need to do it once)
sudo systemctl start nginx
