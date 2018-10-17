"""
    sphinxcontrib.stuffcounter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A sphinx extension to count stuff.

    :copyright: Copyright 2018 by Louis Paternault <spalax+python@gresille.org>
    :license: GPLv3+, see LICENSE for details.
"""

import pbr.version

__version__ = pbr.version.VersionInfo("stuffcounter").version_string()


def setup(app):
    return {"version": __version__, "parallel_read_safe": True}
