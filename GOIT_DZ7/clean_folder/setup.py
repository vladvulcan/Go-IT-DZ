from setuptools import setup, find_namespace_packages

setup (
    name = 'sort_trash',
    version = 1.0,
    description='Этот скрипт сделан в ДЗ №6 и сортирует файлы и папки по категориям',
    author='Wildrider07',
    packages= find_namespace_packages(),
    entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:main']}

)