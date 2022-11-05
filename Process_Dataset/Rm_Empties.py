# copy this file into the folder that contain all the VisDrone annotation file , then run it with python
import string, os
import pdb
import argparse
import re

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
parser = argparse.ArgumentParser()
parser.add_argument('--label_path', type=dir_path)
parser.add_argument('--image_path', type=dir_path)
args = parser.parse_args()
del_path = []
for roots,dirs,files in os.walk(args.label_path, topdown=True):
	for f in files:
		full_path = str(roots)+'/'+str(f)
		if (os.stat(full_path).st_size == 0):
			del_path.append(full_path)
			os.remove(full_path)
			print("Removing -> " + str(full_path))
for path in del_path:
	#".*annotations\(Yolo\)\/(.*)\.txt"
	corrected_path = str(args.image_path) +"/"+ str(re.findall("annotations/(.*)\.txt",str(path))[0])+".jpg"
	os.remove(corrected_path)
	print("Remove also " + corrected_path )
