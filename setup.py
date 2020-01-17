from setuptools import find_packages, setup

entry_point = (
    "csvReader = csvReader:csvReader"
)

# # get the dependencies and installs
# with open("requirements.txt", "r", encoding="utf-8") as f:
#     requires = [x.strip() for x in f if x.strip()]

setup(
    name="CSV Reader for McCord",
    version="0.1",
    author="Matthew Kennedy",
    packages=find_packages(),
    entry_points={"console_scripts": [entry_point]},
    # install_requires=requires,
)
