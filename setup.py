from setuptools import find_packages, setup

setup(
    name='lidarts',
    version='0.4.0-34',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'alembic',
        'bcrypt',
        'bleach',
        'coverage',
        'eventlet',
        'Flask-BabelEx',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Migrate',
        'Flask-Moment',
        'Flask-Security',
        'Flask-SocketIO',
        'Flask-SQLAlchemy',
        'Flask-Uploads',
        'Flask-WTF',
        'gunicorn',
        'hashids',
        'numpy',
        'psycopg2-binary',
        'pytest',
        'python-dotenv',
        'redis'
    ],
)
