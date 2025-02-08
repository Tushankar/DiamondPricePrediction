from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]

    return requirements

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="tushankar",
    author_email="sahatushankar234@gmail.com",
    install_requires=get_requirements("requirement.txt"),
    packages=find_packages(),
)
