#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get install -y python3-pip libjpeg8-dev postgresql postgresql-contrib libpq-dev libsqlite3-dev nodejs npm

sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g bower

mkdir /home/vagrant/git-sources
wget -P /home/vagrant/git-sources https://github.com/python/cpython/archive/v3.4.5.tar.gz
tar -xvf /home/vagrant/git-sources/v3.4.5.tar.gz -C /home/vagrant/git-sources

cd /home/vagrant/git-sources/cpython-3.4.5
./configure --enable-loadable-sqlite-extensions
make
sudo make install

pip3 install --upgrade pip
sudo pip3 install virtualenv
mkdir /home/vagrant/virtualenv
virtualenv -p python3.4 /home/vagrant/virtualenv/pynsk.ru
sudo /home/vagrant/virtualenv/pynsk.ru/bin/pip install -r /vagrant/requirements.txt