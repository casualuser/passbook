from setuptools import setup

version = __import__('passbook').__version__

setup(
    name='Passbook',
    version=version,
    author='Fernando Aramendi',
    author_email='fernando@devartis.com',
    packages=['passbook', 'passbook.test'],
    url='http://github.com/devartis/passbook/',
    license=open('LICENSE.txt').read(),
    description='Passbook file generator',
    long_description=open('README.md').read(),

    download_url='http://pypi.python.org/packages/source/P/Passbook/Passbook-%s.tar.gz' % version,

    install_requires=[
        'cryptography==3.3.1',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
