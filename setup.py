from setuptools import find_packages, setup

setup (
    name = 'ML_PRoject',
    version = '0.0.1',
    author = 'Soumyadeep Dey',
    email = 'soumyadeep.dey162003@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'tensorflow', 'keras'],
    license = 'MIT'
)