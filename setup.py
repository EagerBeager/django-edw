#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools.command.install import install as st_install
from setuptools import setup, find_packages
import backend.edw

try:
    from pypandoc import convert
except ImportError:
    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


def _post_install(dir):
    print('POST INSTALL', dir)


class install(st_install):
    def run(self):
        pass
        """
        st_install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")
        """


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="InfoLabs LLC",
    author_email="team@infolabs.ru",
    name="django-edw",
    version=backend.edw.__version__,
    description="A RESTful Django Enterprise Data Warehouse",
    long_description=convert('README.md', 'rst'),
    url='http://excentrics.github.io/django-edw',
    license='GPL v3 License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['example', 'docs']),
    package_dir={'edw': 'backend/edw', 'email_auth': 'backend/email_auth', 'test_edw': 'backend/test_edw'},
    include_package_data=True,
    zip_safe=False,
    cmdclass={'install': install},
    install_requires=[
        'Django>=1.9,<1.10',
        'djangorestframework>=3.3',
        'beautifulsoup4>=4.4.0',
        'django-post-office>=2.0.5',
        'django-filer>=1.0.6',
        #'django-ipware>=1.1.1',
        'django-fsm>=2.2.1',
        'django-rest-auth>=0.5.0',
        'django-angular>=0.7.15',
        'django-select2>=5.5.0',
        'djangorestframework-recursive==0.1.1',
        'djangorestframework-filters==0.8.0',
        #'django-sass-processor>=0.3.4',
    ],
)