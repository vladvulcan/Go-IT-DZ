from setuptools import setup


def do_setup(args_dict, requires):
    setup(**args_dict,
          install_requires=requires)