from setuptools import setup

setup(name='PowerBI_refresher-NPP',
      version='1.0',
      description='Script for refreshing and publishing Power BI workbooks',
      url='https://github.com/NilPujolPorta/PowerBI_refresher-NPP',
      author='Nil Pujol Porta',
      author_email='nilpujolporta@gmail.com',
      license='GNU',
      packages=['PowerBI_refresher-NPP'],
      install_requires=[
          'pywinauto',
          'psutil',
          'keyboard',
          'argparse',
          'time',
          'os',
          'sys'
      ],
	  entry_points = {
        "console_scripts": ['PowerBI_refresher-NPP = refresher.refresh:main']
        },
      zip_safe=False)
