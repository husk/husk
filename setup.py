import husk
from setuptools import setup, find_packages

kwargs = {
    'packages': find_packages(),
    'include_package_data': True,
    'test_suite': 'tests',
    'name': 'husk',
    'version': husk.__version__,
    'author': 'Byron Ruth, Patrick Henning',
    'author_email': 'b@devel.io',
    'description': husk.__doc__,
    'license': 'BSD',
    'keywords': 'note-taking Cornell',
    'url': 'https://bruth.github.com/husk/',
    'scripts': ['bin/husk'],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7'
    ],
}

setup(**kwargs)
