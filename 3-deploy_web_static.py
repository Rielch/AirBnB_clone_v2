#!/usr/bin/python3
"""Script that does the deployment"""
import os
from datetime import datetime
from fabric.api import env, local, run, put


env.hosts = ['34.139.167.198', '34.138.129.5']


def do_pack():
    """Generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        n = datetime.now()
        fname = "versions/web_static_" + n.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -cvzf " + fname + " web_static")
        return fname
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            filename = archive_path.split('/', 1)
            no_ext = filename[1].split('.', 1)
            f_name = no_ext[0]
            run("mkdir -p /data/web_static/releases/" + f_name + "/")
            run("tar -zxf /tmp/" + filename[1] +
                " -C /data/web_static/releases/" +
                f_name + "/")
            run("rm /tmp/" + filename[1])
            run("mv /data/web_static/releases/" + f_name +
                "/web_static/* /data/web_static/releases/" + f_name + "/")
            run("rm -rf /data/web_static/releases/" + f_name + "/web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/" + f_name +
                "/ /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    file_name = do_pack()
    if not file_name:
        return False
    return do_deploy(file_name)
