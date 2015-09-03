#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from opml2html import __author__, __version__, __license__

setup(
        name             = 'opml2html',
        version          = __version__,
        description      = 'OPML format to HTML format',
        license          = __license__,
        author           = __author__,
        author_email     = '',
        url              = '',
        keywords         = 'opml html',
        packages         = find_packages(),
        install_requires = [],
        )
