CUR_DIR=$(pwd)

sed 's|%ROOT_DIR%|'$CUR_DIR'|g' etc/nginx.conf.tmpl > etc/nginx.conf
sed 's|%ROOT_DIR%|'$CUR_DIR'|g' etc/gunicorn.conf.tmpl > etc/gunicorn.conf
sed 's|%ROOT_DIR%|'$CUR_DIR'|g' etc/django.conf.tmpl > etc/django.conf
sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s $CUR_DIR/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
chmod -R 777 ${CUR_DIR}
#sudo ln -s $CUR_DIR/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo rm   /etc/gunicorn.d/django
sudo ln -s $CUR_DIR/etc/django.conf   /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

