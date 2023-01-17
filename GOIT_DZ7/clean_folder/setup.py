from setuptools import setup, find_namespace_packages

setup (
    name = 'sort_trash',
    version = 1.0,
    author='Wildrider07',
    packages= find_namespace_packages(),
    entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:main']}

)