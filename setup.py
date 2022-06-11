import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="btwim",
	version="0.0.3",
	author="Hyeon Jeon",
	author_email="hj@hcil.snu.ac.kr",
	description="Implementation of between dataset internal measures",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/hj-n/btw-dataset-internal-measures",
	classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.8",
)