from setuptools import setup
import versioneer

setup(
    name='morphocut',
    packages=['morphocut'],
    include_package_data=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=[
        'flask',
        'psycopg2-binary',
        'pandas',
        'sqlalchemy',
        'etaprogress',
        'h5py>=2.8.0',
        'scikit-learn',
        'scipy',
        'redis',
        'rq',
        'hiredis',
        'flask-restful',
        'alembic',
        'Flask-SQLAlchemy',
        'flask-redis',
        'Flask-Migrate',
        'flask-user',
        'timer_cm',
        'fire',
        'Flask-Cors',
        'pytest',
        'coverage',
        'pytest-cov',
        'tqdm',
        'parse',
        'scikit-image',
        'opencv-python==3.4.3.18',
        'opencv-contrib-python==3.4.3.18',
        'pillow-simd',
    ],
)
