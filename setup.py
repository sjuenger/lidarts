from setuptools import find_packages, setup

setup(
    name='lidarts',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'alembic',
        'coverage',
        'eventlet',
        'Flask-Babel',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Migrate',
        'Flask-SocketIO',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'gunicorn',
        'hashids',
        'psycopg2-binary',
        'pytest',
        'python-dotenv',
    ],
)