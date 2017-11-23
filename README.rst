==========================
knytt-stories-desaturation
==========================
Utility that simplifies the process of creating desaturation steps of sprites for the `Knytt Stories <http://nifflas.ni2.se/?page=Knytt+Stories>`_ level editor.


.. contents:: Table of Contents
.. section-numbering::


------------
Installation
------------
1. Download repository as zip.
2. Unpack zip into folder.
3. Enter folder.
4. Run the following command: ::

        $ pip install .


------------------
Additional Options
------------------
Generated output from the command-line argument ``ksdesaturation --help``.

::

	usage: ksdesaturation [-h] [-s [2-255]] input output

	Desaturate images in a given directory based on the naming convention of Knytt
	Stories. Any image matching the naming convention will be desaturated five
	steps from full-color to black-white. The number at the end of the filename
	will be incremented by one for each step. If there is an overlap in names they
	will simply be written over so make sure that the names have enough separation
	in their number intervals.

	positional arguments:
	  input                 directory to look for image to desaturate
	  output                directory to store the desaturated images, the path
	                        will match that given from input except with the given
	                        directory as root, directories will be created if they
	                        don't exist

	optional arguments:
	  -h, --help            show this help message and exit
	  -s [2-255], --steps [2-255]
	                        number of desaturation steps for each input image,
	                        defaults to 5
