from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Geane Alves",
    author_email="geanedarc2@gmail.com",
    description="Sobreposição e fusão de imagens.",
    long_description=Exercicio de processamento de imagens do curso de Python do curso de Processamento de imagens com Pytons.",
    long_description_content_type="text/markdown",
    url="link_para_o_seu_repositorio_github",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)