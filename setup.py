from setuptools import setup, find_packages

setup(
    name="sso_engine_eggpine84",
    version="2.0.0",
    author="Logic_Architect_eggpine84",
    author_email="eggpine84@gmail.com",
    description="NHE S_s[N]_O Polymorphic Direct-to-Silicon Logic Architecture Simulator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eggpine84/sso-engine", # 실제 생성할 깃허브 주소
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free For Non-Commercial Use", # CC BY-NC-ND 4.0 반영
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)