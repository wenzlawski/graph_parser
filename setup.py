# Copyright 2022 by Hitachi, Ltd.
# All rights reserved.

from setuptools import setup

setup(
    name='graph_parser',
    version='0.0.6',
    description='Graph-based parser for argument mining and opinion mining',
    url='https://github.com/hitachi-nlp/graph_parser',
    author='Gaku Morio',
    author_email='gaku.morio.vn@hitachi.com',
    license='CC BY-NC-SA',
    install_requires=[
        'numpy',
        'scipy',
        'setuptools==59.5.0',
        'typer',
        'typer-cli',
        'pandas>=1.0.5',
        'transformers==4.15.0',
        'torch==1.9.0',
        'tensorboard>=2.3.*',
        'tensorflow==2.3.*',
        'keras',
        'coloredlogs>=14.0',
        'jq>=1.0.2',
        'timeout_decorator==0.4.1',
        'click==7.1.2',
        'registrable==0.0.4',
        'psutil==5.7.2',
        'joblib==0.17.0',
        'graphviz==0.14.2',
        'mtool @ git+https://github.com/cfmrp/mtool.git',
        'networkx==2.3',
        'lxml',
        'pydot==1.4.2',
        'sentencepiece==0.1.96',
        'fastapi',
        'uvicorn',
        'starlette',
    ],
    packages=[],
    zip_safe=False,
    entry_points=dict(),
)