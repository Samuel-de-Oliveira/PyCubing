from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='PyCubing',
    version='0.1',
    author='Samuel de Oliveira',
    author_email='samwolfg12@gmail.com',
    description='A Python module to make speedcubing projects a piece of cake',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Samuel-de-Oliveira/PyCubing',
    project_urls={
        'Bug Tracker': 'https://github.com/Samuel-de-Oliveira/PyCubing/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'PyCubing': 'PyCubing'},
    packages=find_packages(where='PyCubing'),
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)
