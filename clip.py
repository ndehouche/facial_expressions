import backprop
import glob
from PIL import Image
import csv
api_key = None
ic = backprop.ImageClassification(api_key=api_key)

images=glob.glob("data/images/*.jpg")

labels = ['happy', 'surprised', 'scared', 'sad', 'angry', 'disgusted', 'pensive']
for image in images:
	Image.open(image).resize((200, 200), Image.NEAREST)
	results = ic(image, labels)
	data = list(results.items())
	with open("output.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		wr.writerow(data)
		print(data)


