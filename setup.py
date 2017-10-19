from setuptools import find_packages, setup


setup(
    name="run_scrumblr",
    version="0.0.1",
    author="Romain Guillebert",
    packages=find_packages(),
    install_requires=["sh"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "run_scrumblr = run_scrumblr.main:main",
        ]
    },
)

