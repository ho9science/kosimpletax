from setuptools import setup, find_packages

setup(
    name             = 'kosimpletax',
    version          = '1.0',
    description      = 'simple tax in Korea',
    author           = 'hyeonki.samdasu',
    author_email     = 'noblesswith@gmail.com',
    url              = 'https://github.com/ho9science/kosimpletax',
    download_url     = 'https://githur.com/ho9science/kosimpletax/archive/master.zip',
    install_requires = [ ],
    packages         = find_packages(),
    keywords         = ['kosimpletax', 'tax', 'korea'],
    python_requires  = '>=3',
    package_data     =  {
    },
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)