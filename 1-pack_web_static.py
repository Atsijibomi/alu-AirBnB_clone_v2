#!/usr/bin/python3
"""We will compress before sending"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Do pack function"""
    local("mkdir -p versions")

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
