from setuptools import setup, find_packages

setup(
    name='instrument_ctrl',
    version='2024.12.09',
    description='Python control of Measurement Instruments under VISA, RS-232, NI PXI and more.',
    long_description = open('README.md').read(),
    author='Pablo GP',
    author_email='pablogonzalezpila@gmail.com',
    url='https://github.com/PaulFilms/instrument_control',
    packages=find_packages(),
    include_package_data=True,
    package_data={'instrument_ctrl': ['INSTRUMENTS/*']}, 
)

# ''' 
# Instrument Control | Python Setup
# '''

# from setuptools import setup, find_packages, Extension

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

# setup(
#     name = "instrument_control",
#     version = '2024.12.09',
#     description="Python control of Measurement Instruments under VISA, RS-232, NI PXI and more.",
#     long_description = "README.md",
#     author = 'Pablo GP',
#     author_email = "pablogonzalezpila@gmail.com",
#     url = "https://github.com/PaulFilms/instrument_control",
#     license = "Apache License",
#     # package_dir={'': 'src'},
#     # packages = find_packages(where='src'), # con find_pachages no conseguir hacerlo funcionar
#     # packages=find_packages(),
#     packages=["instrument_control"],
#     include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
#     package_data={'instrument_control': ['INSTRUMENTS/*']}, 
#     install_requires=requirements,
#     # classifiers = [
#     #     'Programming Language :: Python :: 3.12',
#     #     "Intended Audience :: Developers",
#     #     "Intended Audience :: System Administrators",
#     #     # "Operating System :: OS Independent",
#     #     "Topic :: Software Development",
#     # ],
# )