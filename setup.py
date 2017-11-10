from setuptools import setup

setup(
	name="knytt-stories-desaturation",
	version="0.0.1",
	description="Desaturate images in a given directory based on the naming convention of Knytt Stories.",
	long_description=open("README.rst").read(),
	url="https://github.com/CairX/knytt-stories-desaturation-py",
	author="CairX",
	author_email="lazycairx@gmail.com",
	license="MIT",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Environment :: Console",

		"Topic :: Multimedia :: Graphics",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",

		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5"
	],
	keywords="knytt stories desaturation sprite image",
	packages=["ksdesaturation"],
	install_requires=["pillow"],
	entry_points={
		"console_scripts": [
			"ksdesaturation=ksdesaturation:main"
		],
	},
)
