from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requiremnets = []
    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets = [req.replace('\n','') for req in requiremnets]

        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
    return requiremnets

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Chakrapani',
    author_email = 'chakrapani3513.a@gmail.com',
    packages = find_packages(),
    install_requies = get_requirements('requirements.txt')
)
