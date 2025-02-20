from setuptools import setup
import PyCubing

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='PyCubing',
    version=PyCubing.__version__,
    author='Samuel de Oliveira',
    author_email='samwolfg12@gmail.com',
    packages=['PyCubing'],
    url='https://github.com/Samuel-de-Oliveira/PyCubing',
    license='MIT',
    description='A Python module to make speedcubing projects a piece of cake.',
    keywords = 'cubing rubik rubik\'s cube solver scramble cube',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["requests==2.32.3"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
)
