#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from flask import Flask
from flask.ext.quik import FlaskQuik, render_template


class QuikTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.debug = True
        quik = FlaskQuik(app)
        self.app = app
        self.quik = quik

        @app.route('/templatefile')
        def template_file():
            return render_template('hello.html', name="quik")

    def tearDown(self):
        pass

    def testRenderTemplateFile(self):
        c = self.app.test_client()
        result = c.get('/templatefile')
        self.assertEqual(result.data, '<h1>quik</h1>\n')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QuikTestCase))
    return suite


if __name__ == '__main__':
    unittest.main()
