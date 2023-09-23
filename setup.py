from setuptools import setup

DESCRIPTION = 'collect-license: Collect license files for packages installed with pip.'
NAME = 'collectlicense'
AUTHOR = 'hamacom2004jp'
AUTHOR_EMAIL = 'hamacom2004jp@gmail.com'
URL = 'https://github.com/hamacom2004jp/collect-license'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.0.1'
PYTHON_REQUIRES = '>=3.8'
INSTALL_REQUIRES = [
    'PyYAML>=6.0.1',
    'pip-licenses>=4.3.3'
]
PACKAGES = [
    'collectlicense',
    'collectlicense.app'
]
KEYWORDS = 'LICENSE.txt LICENSE Collect'
CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)