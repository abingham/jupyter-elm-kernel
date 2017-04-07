from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='elm_kernel',
    version='0.1',
    packages=['elm_kernel'],
    description='Jupyter kernel for executing Elm code',
    long_description=readme,
    author='Austin Bingham',
    author_email='austin@sixty-north.com',
    url='https://github.com/abingham/jupyter-elm-kernel',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['jupyter'],
)
