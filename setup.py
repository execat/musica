from distutils.core import setup

setup(
    name='musica',
    version='0.0.1',
    description = 'musica is a Python tool for working with musical notations and scores.',
    author = 'Anuj More',
    author_email = 'anujmorex@gmail.com',
    url = 'https://github.com/execat/musica',
    keywords = 'music composition',
    packages=['musica',],
    license='GPL',
    long_description=open('README.txt').read(),
)