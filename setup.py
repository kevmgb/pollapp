import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_polls_tutorial_v',
    version='1.2.6',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    author='kevin',
    author_email='kevin@kev.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',

    ],
    install_requires=[
        'Django==2.2.2',
        'django-nose==1.4.6',
        'pytest-django==3.5.0',
        'django-pytest==0.2.0',
        
    ],
    scripts=[
        "bin/docs_app"
    ],
)