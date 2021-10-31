#importing requests library
import requests

#asks the user for the link of file to be downloaded

#fetches the bytes


def download(url, fileName, ext):
	bytes = requests.get(url).content
	file = "downloads/" + fileName + ext
	with open(file, 'wb') as doc:
		doc.write(bytes)
		print('Downloaded Successfully')
	
	

#Asks user for the file type
try:
	fileType = input('Which of the following file type do you want to download? \n Music \n Video \n Image \n WebPage \n File Type : ')
	url = input('Please Input the url : ')
	fileName = input('Save file as : ')
	
	if fileType.lower() == "music":
		download(url, fileName, ext='.mp3')
	elif fileType.lower() == "video":
		download(url, fileName, ext='.mp4')
	elif fileType.lower() == "image":
		download(url, fileName, ext='.jpeg')
	elif fileType.lower() == "webpage":
		download(url, fileName, ext='.html')
		
except:
	print('An Error occured')