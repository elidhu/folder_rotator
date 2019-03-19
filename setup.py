from setuptools import setup, find_packages

setup(
    name='FolderRotator',
    version='0.0.1',
    packages=find_packages(),
    author='Kevin Glasson',
    author_email='kevinglasson+folderrotator@gmail.com',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner"
    ],
    tests_require=[
        "pytest==4.3.",
        "pytest-sugar==0.9.2"
    ],
    python_requires='>3.6'
)
