#!/usr/bin/python3
""" Script that compress files using .tgz"""
from fabric.operations import local
from datetime import datetime

def do_pack():
    """function to compress files """
    local("mkdir -p versions")
    return_command = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if return_command.failed:
        return None
    return return_command
