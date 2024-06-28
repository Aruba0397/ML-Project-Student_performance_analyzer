from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOt ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOt in requirements:
            requirements.remove(HYPEN_E_DOt)

    return requirements
setup(
name='Student Performance Analyzer',
version='0.0.1',
author='Aruba',
author_email='aruba0397@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')




)