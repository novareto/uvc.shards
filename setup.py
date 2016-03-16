# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = "0.1"

install_requires = [
    'Chameleon >= 2.4',
    'setuptools',
    'zope.component',
    ]

tests_require = [
    'zope.component',
    'zope.interface',
    ]

setup(
    name='uvc.shards',
    version=version,
    author='Novareto',
    author_email='',
    url='',
    download_url='http://pypi.python.org/pypi/uvc.shards',
    description='UVC View Sharding',
    long_description=(open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read()),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
        },
    entry_points="""
    # -*- Entry points: -*-
    [chameleon.tales]
    shard = uvc.shards.shard:ShardExpr
    """,
    )
