from setuptools import setup, find_packages

setup(
    name='django-mongodb-cash-backend',
    version='2020.2.18',
    packages=['django_mongodb_cash_backend'],
    package_dir={'django_mongodb_cash_backend': 'django_mongodb_cash_backend'},
    provides=['django_mongodb_cash_backend'],
    include_package_data=True,
    url='https://github.com/Alir3z4/django-mongodb-cash-backend',
    license=open('LICENSE').read(),
    author='Karol Sikora',
    author_email='karol.sikora@laboratorium.ee',
    maintainer='Alireza Savand',
    maintainer_email='alireza.savand@gmail.com',
    description='The only Django MongoDB Cache backend you need.',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django~=1.11.13',
        'pymongo~=3.6.1'
    ],
    keywords=[
        'django',
        'web',
        'cache',
        'mongodb'
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development'
    ],
)
