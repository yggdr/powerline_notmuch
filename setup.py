from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='powerline_notmuch',
    version='0.1',
    description='Query your notmuch database from powerline',
    long_description=long_description,
    url='https://github.com/yggdr/powerline_notmuch',
    author='Konstantin Schukraft',
    author_email='konstantin@schukraft.org',
    license='ISC',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: ISC License (ISCL)',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Communications :: Email'
    ],
    keywords='powerline notmuch email',
    platforms='any',
    packages=['powerline_notmuch'],
)
