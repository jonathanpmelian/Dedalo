from setuptools import setup, find_packages

# Helper function to read requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
    
setup(
  name="static-site-generator",
  version="0.1",
  packages=find_packages(where="."),
  entry_points={
    "console_scripts": [
      "ssg=src.cli:main"
    ]
  },
  install_requires=parse_requirements("requirements.txt")
)