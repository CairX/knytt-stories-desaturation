import re
from PIL import Image, ImageEnhance

paths = [
	#"Tileset255.png",
	#"Tileset250.png",
	#"Tileset245.png",
	#"Tileset240.png",
	#"Gradient46.png"
]

pattern = re.compile(r"(\w+?)(\d+)(.\w+)", re.IGNORECASE)

for path in paths:
	original = Image.open("basic/" + path)
	original.save(path)

	m = pattern.match(path)

	converter = ImageEnhance.Color(original)
	for index in range(1, 5):
		copy = converter.enhance(1 - 0.25 * index)
		copy.save(m.group(1) + "" + str(int(m.group(2)) - index) + m.group(3))
