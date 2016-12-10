from setuptools import setup,find_packages

setup(
    name="demo",
    version= "0.1",
    packages=find_packages("src"),
    package_dir={"":"src"},
    package_data={
        "":["*.txt"],
        "demo":["data/*.dat"]},
    zip_safe=True
    )