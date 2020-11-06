# https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding="utf-8")

setup(
    name='bad',
    version="0.0.1",
    description="Branch Analysis Diagram (BAD) generated a dendrogram of git branches",
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='pypa url',
    author='Zach Buckley',
    author_email='buckley.zach@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
    ],
    keywords='development, git',
    packages=find_packages(where='./'),
    python_requires='>=3.5, <4',
    install_requires=[
        'GitPython',
    ],
    entry_points={
        'console_scripts': [
            'bad=Bad.bad:main',
        ]
    },
    # TODO project urls
)