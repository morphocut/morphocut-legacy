from setuptools import setup
import versioneer

setup(
    name='morphocut',
    packages=['morphocut'],
    include_package_data=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=[
        'numpy',
        'pillow-simd',
        'scikit-image',
        # 'pandas',
        # 'sqlalchemy',
        # 'h5py>=2.8.0',
        # 'scikit-learn',
        # 'scipy',
        # 'timer_cm',
        # 'pytest',
        # 'coverage',
        # 'pytest-cov',
        # 'tqdm',
        # 'parse',
        # 'opencv-python==3.4.3.18',
        # 'opencv-contrib-python==3.4.3.18',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }
)
