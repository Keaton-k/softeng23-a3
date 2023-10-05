from setuptools import find_packages, setup

setup(
    name="FIXME",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "FIXME=FIXME.__main__:main",
        ]
    },
)
