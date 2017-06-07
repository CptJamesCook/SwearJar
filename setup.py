from setuptools import setup, find_packages


setup(
    name="SwearJar",
    version="0.0",
    packages=find_packages(),
    scripts=['run.py'],

    # States we are using nose2 for testing
    test_suite='nose2.collector.collector',

    # put dependencies here
    install_requires=['numpy', 'scipy', 'pyqt5', 'matplotlib'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author="James Cook",
    author_email="mrniceguyjames@gmail.com",
    description="Make graphs based on who's been swearing in the office.",
    license="MIT",
    url="https://github.com/CptJamesCook/SwearJar",
)

if __name__ == "__main__":
    pass
