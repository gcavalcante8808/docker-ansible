#!/bin/bash

set -e

if [ ! -d /home/webserver/.ssh/id_rsa ]; then
    echo "No Private Key Provided. Creating one ..."
    yes "" | ssh-keygen -t rsa -N "" -f /home/webserver/.ssh/id_rsa
fi

for f in /docker-entrypoint-initdb.d/*; do
	case "$f" in
		*.sh)     echo "$0: running $f"; . "$f" ;;
		*)        echo "$0: ignoring $f" ;;
	esac
	echo
done

while true; do sleep 1000; done
