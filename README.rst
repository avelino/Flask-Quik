==========
Flask-Quik
==========

.. image:: https://travis-ci.org/avelino/Flask-Quik.png?branch=master
    :target: https://travis-ci.org/avelino/Flask-Quik
    :alt: Build Status - Travis CI

Provides support for Quik Templates in Flask - https://github.com/avelino/quik



Registration
============

Applications can be registered directly in the extension constructor::

    from flask import Flask
    from flask.ext.quik import FlaskQuik

    app = Flask(__name__)
    quik = FlaskQuik(app)



Rendering
=========

Rendering Quik templates sends the same :data:`~flask.template_rendered` signal
as Jinja2 templates. Additionally, Quik templates receive the same context as
Jinja2 templates. This allows you to use the same variables as you normally
would (``g``, ``session``, ``url_for``, etc)::

    from flask.ext.quik import render_template

    @app.route('/')
    def hello_quik():
        return render_template('hello.html', name='quik')
