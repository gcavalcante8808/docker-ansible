#!/bin/bash

set -e

if [ ! -d /home/webserver/.ssh/id_rsa ]; then
    echo "No Private Key Provided. Creating one ..."
    yes "" | ssh-keygen -t rsa -N "" -f /home/webserver/.ssh/id_rsa
fi

while true; do sleep 1000; done
