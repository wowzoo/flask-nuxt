#!/usr/bin/env bash

cmd=$1

cd /home/pi/Development/workshop/flask-backend || return
source ./config/gunicorn.conf

if [[ "$cmd" == "start" ]]; then
    # Start backend server
    state="$(ps aux | grep gunicorn | grep ${GUNICORN_SERVER})"
    if [[ ! -z "$state" ]]; then
        echo "backend server is already active. use restart"
    else
        sudo service gunicorn-backend start
    fi

elif [[ "$cmd" == "restart" ]]; then
    # Restart backend server
    sudo service gunicorn-backend restart

elif [[ "$cmd" == "stop" ]]; then
    # Stop backend server
    sudo service gunicorn-backend stop

elif [[ "$cmd" == "status" ]]; then
    # Status for backend server
    state="$(ps aux | grep gunicorn | grep ${GUNICORN_SERVER})"
    if [[ ! -z "$state" ]]; then
        echo "backend server is active"
        ps aux | grep gunicorn | grep ${GUNICORN_SERVER}
        echo ""
    else
        echo "backend server is inactive"
    fi

else
    echo "${cmd} is not valid command"
fi
