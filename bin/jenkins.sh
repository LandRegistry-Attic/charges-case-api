#! /usr/bin/env bash

env_dir="$JENKINS_HOME/virtualenv/${JOB_NAME// /_}"

#create and activate a virtualenv
virtualenv $env_dir
. $env_dir/bin/activate

#install requirements
pip install -r requirements.txt

#install test only requirements
pip install -r requirements_test.txt

#ensure submodules are cloned
git submodule update --init

createdb --owner=$USER --host=192.168.248.73 --username=$USER -W $PASSWORD  $JOB_NAME

DATABASE_URI=postgres://192.168.248.73/$JOB_NAME python run.py db upgrade head

DATABASE_URI=postgres://192.168.248.73/$JOB_NAME coverage run --source=app tests.py --xml

dropdb $JOB_NAME

test_pass=$?

coverage xml
coverage -rm

exit $test_pass
