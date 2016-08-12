Ansible Container
=================

This is a gcavalcante8808/ansible docker image with Ansible Installed. it's Base on Debian:jessie official image.

Build the image
===============

```
    docker build -t gcavalcante8808/ansible .
```

Usage
=====

```
    docker run \
    -d \
    --name ansible \
    gcavalcante8808/ansible
```

After that, you can access the container and run ansible-playbook and other commands through the following way:

```
    docker exec -it ansible bash
```	

Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)

