#!/usr/bin/env python
from setuptools import setup, find_packages


# Parse version number from amis-admin-theme-editor/__init__.py:
with open('amis_admin_theme_editor/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('version'):
            exec(line, info)
            break

setup_info = dict(
    name='amis-admin-theme-editor',
    version=info['version'],
    author='Stefan Welcker',
    author_email='stefan@u2d.ai',
    url='https://github.com/swelcker/amis-admin-theme-editor',
    download_url='http://pypi.python.org/pypi/amis-admin-theme-editor',
    amis_admin_theme_editor_urls={
        'Source': 'https://github.com/swelcker/amis-admin-theme-editor',
        'Tracker': 'https://github.com/swelcker/amis-admin-theme-editor/issues',
    },
    description='amis-admin-theme-editor - CSS Theme Editor for fastapi-amis-admin, includes definitions for cxd, antd, ang and dark theme of amis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['amis_admin_theme_editor'] + ['amis_admin_theme_editor.' + pkg for pkg in find_packages('amis_admin_theme_editor')],

    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
    include_package_data=True
)

setup(**setup_info)
