#!/bin/bash
#

PROJECT_NAME='ratings'

# Install PIP via Distribute
cd /tmp/
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
easy_install pip
sudo rm /tmp/*.gz
sudo rm /tmp/*.py

sudo apt-get update

# Install git
sudo apt-get install -y git

# Install requirements
sudo pip install -r /Developer/Projects/$PROJECT_NAME/requirements.txt
