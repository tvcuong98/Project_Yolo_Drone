# copy this file into the folder that contain all the VisDrone annotation file , then run it with python
import string, os
import pdb
import argparse

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=dir_path)
args = parser.parse_args()
def find_x(bbox_left,image_width,box_xmax):
	image_width = 1.0 * int(image_width)
	absolute_x = int(bbox_left) + 0.5 * (int(box_xmax) - int(bbox_left))
	x = absolute_x / image_width
	return str(x)
def find_y(image_height,box_ymax,bbox_top):
	image_height = 1.0 * int(image_height)
	absolute_y = int(bbox_top) + 0.5 * (int(box_ymax) - int(bbox_top))
	y = absolute_y / image_height
	return str(y)

def find_width(box_xmax,bbox_left,image_width): 
	absolute_width = int(box_xmax) - int(bbox_left)
	image_width = 1.0 * int(image_width)
	width = absolute_width / image_width 
	return str(width)


def find_height(bbox_top,box_ymax,image_height):
	absolute_height = int(box_ymax) - int(bbox_top)
	image_height = 1.0 * int(image_height)
	height = absolute_height / image_height
	return str(height)

for f in os.listdir(args.path):
	if f != "VisDrone_to_Yolo_Annotation.py":
		fname = str(args.path)+"/"+f
		fname_out = str(args.path)+"/"+f

		
		image_width = 1920
		image_height = 1080

		content = []

		with open(fname) as f:
			content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		content = [x.strip() for x in content] 

		new_content = []
		for x in content:
			print(x)
			print(type(x))
			y = x.split(",")
			print(y)
			print(type(y))
			bbox_left = float(y[0])
			bbox_top = float(y[1])
			bbox_width = float(y[2])
			bbox_height = float(y[3])
			box_xmax = str(int(bbox_left) + int(bbox_width))
			box_ymax = str(int(bbox_top) + int(bbox_height))

			place_0_value = y[5]
			place_1_value = find_x(bbox_left,image_width,box_xmax)
			place_2_value = find_y(image_height,box_ymax,bbox_top)
			place_3_value = find_width(box_xmax,bbox_left,image_width)
			place_4_value = find_height(bbox_top,box_ymax,image_height)

			output = str(place_0_value) + " " + str(place_1_value) + " " + str(place_2_value) + " " + str(place_3_value) + " " + str(place_4_value)
			new_content.append(output)

		

		with open(fname_out, 'w') as f:
			f.truncate(0)
			for item in new_content:
				f.write("%s\n" % item)
