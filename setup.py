from setuptools import setup

name = 'pwkeeper'
VERSION = '1.1.0'

setup(
    name=name,
    packages=[name],
    version=VERSION,
    description='Simple terminal-based password manager',
    long_description='See https://github.com/kvikshaug/pwkeeper/blob/master/README.md',
    author='Ali Kaafarani',
    author_email='ali@kvikshaug.no',
    url='https://github.com/kvikshaug/pwkeeper/',
    download_url='https://github.com/kvikshaug/pwkeeper/tarball/v%s' % (VERSION),
    keywords=['password', 'password-manager', 'terminal'],
    license='WTFPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['pycrypto>=2.6.1,<3'],
    entry_points={
        'console_scripts': [
            'pw = pwkeeper.pwkeeper:main',
        ],
    },
)
