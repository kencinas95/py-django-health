from distutils.core import setup

setup(
  packages=['health', 'health.checkers'],
  version='1.0.0',
  license='MIT',
  url='https://github.com/kencinas95/health',
  keywords=['health', 'checkers', 'heartbeat', 'microservices'],
  install_requires=[
    'django',
    'pydantic'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ]
)
