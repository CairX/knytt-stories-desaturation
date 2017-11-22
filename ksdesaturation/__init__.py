import argparse
import os
import re
from PIL import Image, ImageEnhance


KNYTT_FILNAME = re.compile(r"(\w+?)(\d+)(.png)", re.IGNORECASE)


def desaturate(input, output, filename, steps):
	filename = KNYTT_FILNAME.match(filename)
	if not filename:
		return

	image = Image.open(os.path.join(input, filename.group(0)))
	os.makedirs(output, exist_ok=True)
	converter = ImageEnhance.Color(image)
	interval = 1 / (steps - 1)

	for index in range(0, steps):
		newname = filename.group(1) + str(int(filename.group(2)) + index) + filename.group(3)
		copy = converter.enhance(1 - interval * index)
		copy.save(os.path.join(output, newname))


def read_directory(input, output, steps):
	for directory, sub_directories, files in os.walk(input):
		for filename in files:
			desaturate(directory, directory.replace(input, output), filename, steps)


def steps_type(x):
	x = int(x)
	if not 2 <= x <= 255:
		raise argparse.ArgumentTypeError("invalid choice: {} (value range from 2 to 255)".format(x))
	return x


def main():
	parser = argparse.ArgumentParser(description="Desaturate images in a given directory based on the naming convention of Knytt Stories. Any image matching the naming convention will be desaturated five steps from full-color to black-white. The number at the end of the filename will be incremented by one for each step. If there is an overlap in names they will simply be written over so make sure that the names have enough separation in their number intervals.")
	parser.add_argument("input", help="directory to look for image to desaturate")
	parser.add_argument("output", help="directory to store the desaturated images, the path will match that given from input except with the given directory as root, directories will be created if they don't exist")
	parser.add_argument("-s", "--steps", type=steps_type, default=5, metavar="[2-255]", help="number of desaturation steps for each input image, defaults to 5")
	args = parser.parse_args()

	read_directory(args.input.rstrip(os.sep), args.output.rstrip(os.sep), args.steps)


if __name__ == "__main__":
	main()
