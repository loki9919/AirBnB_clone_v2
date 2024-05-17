#!/usr/bin/python3
"""
Script to genereate tgz archive
fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    do an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    generate = local('tar -cvzf versions/{} web_static'.format(archive))
    if generate is not None:
        return archive
    else:
        return None
