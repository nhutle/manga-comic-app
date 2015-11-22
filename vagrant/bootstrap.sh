#/bin/bash

### Linux Base Packages
sudo apt-get -y update
sudo apt-get -y install build-essential vim curl git tmux libbz2-dev unzip
sudo apt-get -y install default-jre


### Image Libraries (needed for pil jpeg support)
sudo apt-get -y install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev


### Install Python
# echo '### Download & Install Python ...'

## Install all python softwares
# sudo apt-get -y install python-pip python-dev libmysqlclient-dev libsqlite3-dev python-mysqldb python-twisted libffi-dev
# sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev tk-dev libgdbm-dev libc6-dev libssl-dev libxml2-dev libxslt1-dev

## Install the latest 2.7.10 version -- scrapy has not supported Python 3 till now.
# mkdir ~/src
# cd ~/src
# wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
# tar -zxvf Python-2.7.10.tgz
# cd Python-2.7.10.tgz
# mkdir ~/.localpython
# ./configure --prefix=/home/vagrant/.localpython  --with-zlib
# make
# make install

### Install PostgreSQL
# sudo apt-get install postgresql postgresql-contrib
# apt-cache search postgres


## Install virtualenv
# echo '### Virtualenv ...'
# sudo pip install virtualenvwrapper

# echo "# setup virtualenvwrapper" >> /home/vagrant/.profile
# echo "export WORKON_HOME=$HOME/.virtualenvs" >> /home/vagrant/.profile
# echo "export PROJECT_HOME=$HOME/Devel" >> /home/vagrant/.profile
# echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.profile

# source /home/vagrant/.profile
# mkvirtualenv env

# echo "workon env" >> /home/vagrant/.profile


### Install heroku toolbelt + app dependencies
cd /manga-comic-app/backend
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
pip install -r requirements.txt