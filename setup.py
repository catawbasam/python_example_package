try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Example Package',
    'author': 'Keith Campbell',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'keithcc1966@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['python_example_package'],
    'scripts': [],
    'name': 'python_example_package'
}

setup(**config)