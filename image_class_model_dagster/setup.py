# from setuptools import find_packages, setup

# setup(
#     name="image_class_model_dagster",
#     packages=find_packages(exclude=["image_class_model_dagster_tests"]),
#     install_requires=[
#         "dagster",
#         "dagster-cloud"
#     ],
#     extras_require={"dev": ["dagster-webserver", "pytest"]},
# )
from setuptools import setup, find_packages

setup(
    name='image_class_model_dagster',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'dagster',
        'torch',  # For deep learning
        'torchvision',  # For datasets and transforms
        'pandas',  # For data manipulation
        'pytest',  # For unit tests
    ],
)
