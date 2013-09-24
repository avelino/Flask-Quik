#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    flask.ext.quik
    ~~~~~~~~~~~~~~

    Extension implementing Quik Templates support in Flask with support for
    flask-babel

    :copyright: (c) 2012 by Thiago Avelino <thiago@avelino.xxx>
    :license: MIT, see LICENSE for more details.
"""
from quik import FileLoader


class FlaskQuik(object):
    """
    Main class for bridging quik and flask. We try to stay as close as possible
    to how Jinja2 is used in Flask, while at the same time surfacing the useful
    stuff from Quik.

    """
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.init_app(app)
        self.app = app

    def init_app(self, app):
        """
        Initialize a :class:`~flask.Flask` application
        for use with this extension. This method is useful for the factory
        pattern of extension initialization. Example::

        quik = FlaskQuik()

        app = Flask(__name__)
        quik.init_app(app)

        .. note::
            This call will fail if you called the :class:`FlaskQuik`
            constructor with an ``app`` argument.
        """
        if self.app:
            raise RuntimeError("Cannot call init_app when app argument was "
                               "provided to FlaskQuik constructor.")

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['quik'] = self

