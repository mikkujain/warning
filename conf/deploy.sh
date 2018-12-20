#!/bin/bash

##
# Deployment script for warning-system.
##

cd /home/teleconsystems
svn co https://atvariance.in/repositories/warning-system/trunk warning-system

cd warning-system
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 manage.py migrate || exit 1
python3 manage.py loaddata slaves/fixture.yml || exit 1
python3 manage.py collectstatic -c --noinput || exit 1

su - root
systemctl restart warningsystem.service
systemctl restart nginx.service
