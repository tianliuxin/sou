from setuptools import setup,find_packages

setup(
    name="sou",
    version="0.1",
    description="借助系统搜索软件进行搜索",
    author="liu.xin",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "sou=sou.sou:main"
        ]
    }
)