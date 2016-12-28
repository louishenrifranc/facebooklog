from setuptools import setup

setup(
    name='messengerlog',
    version='0.1.0',
    description='A simple logger that duplicates console logs and send it to your Facebook account.',
    url='http://github.com/louishenrifranc/messengerlog',
    author='Louis Henri Franc',
    author_email='louis-henri.franc@polymtl.ca',
    license='MIT',
    packages=['messengerlog'],
    install_requires=[
        'fbchat',
        'matplotlib',
        ''
    ],
    zip_safe=False
)
