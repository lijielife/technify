from distutils.core import setup
setup(
  name = 'technify',
  packages = ['technify'],
  version = '0.5',
  description = 'A framework to run technical analysis. Powered by pandas.',
  author = 'Ruben Afonso',
  author_email = 'rbfrancos@gmail.com',
  url = 'https://github.com/rubenafo/technify', 
  download_url = 'https://github.com/rubenafo/technify/archive/0.5.zip',
  keywords = ['technical-analysis', 'pandas', 'finance','stock'],
  classifiers = [],
  install_requires = ["yfm", "quandl"]
)

