import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysgl",
    version="0.0.1",
    author="Prof. Andrea Pollini",
    author_email="prof.andrea.pollini@gmail.com",
    description="Simple PyGame based  OO Library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProfAndreaPollini/pysgl.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
)
