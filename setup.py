import io

import re
from setuptools import setup, find_packages


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


version_file_name = "consolemenu/version.py"
version_file_contents = open("consolemenu/version.py", "rt").read()
version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(version_regex, version_file_contents, re.M)
if match:
    __version__ = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (version_file_name,))

setup(
    name='console-menu',
    version=__version__,
    url='http://github.com/aegirhall/console-menu',
    license='MIT',
    author='Aegir Hall',
    author_email='aegirhall@gmail.com',
    description='A simple console menu system',
    long_description=read("README.rst", "CHANGELOG.rst"),
    packages=find_packages(),
    install_requires=['six'],
    # setup_requires=['pytest-runner'],
    # tests_require=['tox'],
    # cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
