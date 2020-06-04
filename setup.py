import setuptools

with open('README.md') as file:
    long_desc = file.read()

setuptools.setup(
    name="instapvapi",
    version="0.0.8",
    author="UWSGI",
    url="https://github.com/its0x4d/instagramapi-python",
    author_email="mosydev2016@gmail.com",
    description="An unofficial instagram private api.",
    packages=setuptools.find_packages(include=['requests', 'colorama', 'packaging', 'redis']),
    platforms=['any'],
    license="MIT",
    long_description="An unofficial instagram private api written in python. Thanks to mgp25.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
