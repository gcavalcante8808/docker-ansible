#!/usr/bin/env python


import sys
import os
import pystache

from git import Repo

# Get the Git Tree
repo = Repo()

# Get current tags
tags = repo.tags

# Gather the Supported Versions and Daemons.
with open('supported_versions', 'r') as openfile:
    supported_versions = [line.rstrip('\n') for line in openfile]

def add_to_git(version):
    """ Add newly created files to git """
    repo.git.add(A=True)
    commit = repo.index.commit('Automatic generation of %s commit' % version)
    tag = [ tag for tag in tags if tag.name == version ]
    if tag:
        print('Tag %s will be removed from local repo' %version)
        repo.delete_tag(version)

    repo.create_tag(version, ref=commit,
                    message="Automatic generation of %s tag" % version)

# Iter over supported daemons and versions, creating the needed directories and using
# mustache to write the new Dockerfile Version.
for version in supported_versions:
    context = {"version": version}

    # Write the New Dockerfile for specific version.
    template_file = 'Dockerfile.mustache'
        
    template = open(template_file, 'r').read()
    with open('Dockerfile', 'w') as tempfile:
        tempfile.write(pystache.render(template, context))
    print('Added %s version support' %version)
    add_to_git(version)

print("All files for supported versions were generated")

