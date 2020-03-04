import sys
import numpy as Np
from PIL import Image

strip_off = 500
block_w = 20
block_h = 20

for f_path in sys.argv[1:]:
	f_name = f_path.split('/')[-1]
	print(f_path)
	image = Image.open(f_path)
	w, h = image.size
	strip = image.crop((0, strip_off, w, strip_off + block_h))
	blocks = Np.zeros(w // block_w + 1, int)
	for i in range(0, block_h):
		for j in range(0, w):
			px = strip.getpixel((j, i))
			blocks[j // block_w] += max(px[0], max(px[1], px[2]))
	print(blocks)
	for i in range(len(blocks)):
		blocks[i] //= block_w * block_h
	print(blocks)
	for i in range(0, block_h):
		for j in range(0, w):
			val = blocks[j // block_w]
			strip.putpixel((j, i), (val, val, val))
	strip.save("out/strip_" + f_name)


	
