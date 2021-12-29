import os
import math

# file=open('test.txt','a')

# F_SIZE1= os.path.getsize('test.txt')

# print(F_SIZE1)

# print(f'File size :kb\n')

# file.write("\nThe name of the best programmer in the world is JayCoder.")

# F_SIZE2= os.path.getsize('test.txt')

# F_SIZE2 /= 1024

# print(f'\nFile size : {round(F_SIZE2,2)} kb')

# print(os.path.getsize('test.txt'))

# FILE=r'D:\Windows.old\Users\joshua\Videos\proj 101\YouTube Go.apk'

# FILE='test.txt'

# FILE=r'C:\Users\jay\Desktop\my-repos\Intensive_kivymd\soke.py'

# def to_byte(path,rand_n):
# 	return ("{:,}".format(round(os.path.getsize(path),rand_n)) , 'bytes')

# def to_kb(path,rand_n):
# 	return ("{:,}".format(round(os.path.getsize(path)/1024,rand_n)), 'kb')

# def to_mb(path,rand_n):
# 	return ("{:,}".format(round((os.path.getsize(path)*1024)/1024,rand_n)), 'mb')

# def to_gb(path,rand_n):
# 	return ("{:,}".format(round((os.path.getsize(path)*1024)/3,rand_n)), 'gb')





FILE=r'D:\Windows.old\Users\joshua\Videos\bootstrap-blog\bootstrap\benita stuffs\Like Stars On Earth Full Movie with English subtitles.mp4'

def convert_to(file,whole,choice,round_to=2):

	STANDARD_SIZE=1024

	_file_size=os.path.getsize(file)

	byte= _file_size
	kb= byte/STANDARD_SIZE
	mb= kb/STANDARD_SIZE
	gb= mb/STANDARD_SIZE

	keys={'byte':byte,'kb':kb,'mb':mb,'gb':gb}

	number=keys[choice]

	rounded_number= round(number,round_to)

	floor_number=math.floor(number)+1
	
	if whole:
		return (floor_number,choice)
	else:
		return (rounded_number,choice)


def file_size(file,r_num=2,unit='',whole=False):
	"""This unittion take take a file path and returns 
	the size of the particular file associated with """

	STANDARD_SIZE=1024

	_file_size=os.path.getsize(file)

	byte= _file_size
	kb= byte/STANDARD_SIZE
	mb= kb/STANDARD_SIZE
	gb= mb/STANDARD_SIZE

	if unit:
		if unit=='byte'or unit=='kb'or unit=='mb' or unit=='gb':
			return convert_to(file,whole,unit)
		else:
			raise KeyError("Invalid unit please enter a correct unit like 'byte' , 'kb' , 'mb' ,'gb'")


	else:
		# Size in byte
		if _file_size <1024:
			return (round(byte,r_num),'byte')

		# size in Kilobyte
		elif kb <1024:
			return (round(kb,r_num),'kb')

		# size in Megabyte
		elif mb < 1024 :
			return (round(mb,r_num),'mb') 

		# size in Gigabyte
		elif gb <1024:
			return 	(round(gb,r_num),'gb') 


# size=file_size(FILE,r_num=2)

# print(size)

#size_to_whole=math.floor(size[0])+1

#print(size_to_whole,size[1])

#r_n=('{:,}'.format(size[0]))

#print(r_n)
base='D://My Phone videos & download/python stuffs/'
file_path=os.listdir(base)

for name in file_path:

	size=file_size(f'{base}/{name}',r_num=2,unit="")

	print(f'{name} : {size}','\n')





