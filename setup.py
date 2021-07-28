import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dev_tools",
    version="0.0.1",  # 本版本可以不进行更新
    author="Daryl.Xu",
    author_email="xuziqiang@zyheal.com",
    description="General dev_tools written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zyheal/dev-tools",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'jinja2'],
    entry_points={
    },
    classifiers=(
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ),
)
