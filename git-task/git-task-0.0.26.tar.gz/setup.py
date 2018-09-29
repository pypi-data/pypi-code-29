import setuptools, subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-task",
    version=subprocess.check_output(["git", "describe", "--tags"]).decode().strip(),
    author="bessbd",
    author_email="bessbd@gmail.com",
    description="Git-task",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bessbd/git-task",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

#TODO git config --global alias.task '!'"groovy $(pwd)/git-task/git-task.groovy"

