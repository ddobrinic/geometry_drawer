from setuptools import setup, find_packages

setup(
    name='geometry_drawer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'shapely'
        ],
    author='Dino Dobrinić',
    author_email='ddobrinic@geof.unizg.hr',
    description='A brief description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ddobrinic/geometry_drawer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
