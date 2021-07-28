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
    license="MIT",
    platforms=['Linux', 'Windows', 'MacOs'],
    packages=setuptools.find_packages(),  # 默认在.目录寻找模块（需要有__init__.py）
    include_package_data=True,
    package_dir={'': '.'},
    install_requires=['flask', 'jinja2'],
    entry_points={
        'console_scripts': [
            'pts = dev_tools.template_server:_main',
            'passer_template_server = dev_tools.template_server:_main',
            ]
    },
    classifiers=(
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ),
)
