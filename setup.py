from setuptools import setup, find_packages


setup(
   name='financial_modelling',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/yellow-bird-consult/financial_modelling",
   description='basic tool to help with financial modelling',
   long_description="basic tool to help with financial modelling",
   package_data={'': ['script.sh']},
   include_package_data=True,
   install_requires=[
       "pandas",
       "jupyter"
   ],
   extras_require={
      "server": []
   },
   entry_points={
       "console_scripts": [
          "cml=camel.interface.entry_points.main_interface:main"
       ]
   },
)