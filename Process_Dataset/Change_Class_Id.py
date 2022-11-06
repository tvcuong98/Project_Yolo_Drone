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
for f in os.listdir(args.path):
	if f != "Just_Car.py":
		fname = str(args.path)+'/'+f
		fname_out = str(args.path)+'/'+f

		
		image_width = 1920
		image_height = 1080

		content = []

		with open(fname) as f:
			content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		content = [x.strip() for x in content] 

		new_content = []
		for x in content: # each x is a line 
			print(x)
			print(type(x))
			y = x.split(" ")
			print(y)
			print(type(y))
			if (float(y[0])==4):
				place_0_value = 0
				place_1_value = y[1]
				place_2_value = y[2]
				place_3_value = y[3]
				place_4_value = y[4]

				output = str(place_0_value) + " " + str(place_1_value) + " " + str(place_2_value) + " " + str(place_3_value) + " " + str(place_4_value)
				new_content.append(output)

		

		with open(fname_out, 'w') as f:
			f.truncate(0)
			for item in new_content:
				f.write("%s\n" % item)
