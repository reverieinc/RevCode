from distutils.core import setup
setup(
  name = 'revcode',
  packages = ['revcode'], # this must be the same as the name above
  version = '1.0',
  description = 'A Roman encoding module for Indian languages',
  author = 'Reverie Language Technologies',
  author_email = 'rajat.prakash@reverieinc.com', ## rajat.prakash@reverieinc.com
  url = 'https://github.com/reverieinc/RevCode.git', # use the URL to the github repo
  keywords = ['Roman Encoding', 'revcode', 'Indic languages', 'Indian languages'], 
  classifiers = [

        'Intended Audience :: Developers',

        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 2.7',
  ],
)