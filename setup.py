# -*- coding: utf-8 -*-
"""Installer for the eteaching.mbr.dataroom package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='eteaching.mbr.dataroom',
    version='1.0a1',
    description="Add on to connect the data room of MeinBildungsraum to Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Markus Schmidt',
    author_email='m.schmidt@iwm-tuebingen.de',
    url='https://github.com/collective/eteaching.mbr.dataroom',
    project_urls={
        'PyPI': 'https://pypi.org/project/eteaching.mbr.dataroom/',
        'Source': 'https://github.com/collective/eteaching.mbr.dataroom',
        'Tracker': 'https://github.com/collective/eteaching.mbr.dataroom/issues',
        # 'Documentation': 'https://eteaching.mbr.dataroom.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['eteaching', 'eteaching.mbr'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = eteaching.mbr.dataroom.locales.update:update_locale
    """,
)
