import sys
import numpy as Np
from PIL import Image


strip_off = 500
block_w = 20
block_h = 20
edge_thres = 200


def norm255(array):
	arr_max = 0
	for i in range(len(array)):
		arr_max = max(array[i], arr_max)
	for i in range(len(array)):
		array[i] *= 255 / arr_max

def thres255(array, value):
	for i in range(len(array)):
		if array[i] > value:
			array[i] = 255
		else:
			array[i] = 0


for f_path in sys.argv[1:]:
	f_name = f_path.split('/')[-1]
	print(f_path)
	image = Image.open(f_path)
	w, h = image.size
	blocks = Np.zeros(w // block_w + 1, float)
	edges = Np.zeros(len(blocks), float)
	for i in range(strip_off, strip_off + block_h):
		for j in range(0, w):
			px = image.getpixel((j, i))
			blocks[j // block_w] += max(px[0], max(px[1], px[2]))
	for i in range(len(blocks)):
		blocks[i] /= block_w * block_h
	for i in range(1, len(blocks) - 1):
		edges[i] = blocks[i-1] - blocks[i] * 2 + blocks[i+1]
	norm255(edges)
	thres255(edges, edge_thres)
	for i in range(strip_off, strip_off + block_h):
		for j in range(0, w):
			val = int(edges[j // block_w])
			image.putpixel((j, i), (val, val, val))
	image.save("out/" + f_name)


	
