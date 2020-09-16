from PIL import Image
import glob
import os, sys
from natsort import natsorted

dirPath = os.path.dirname(sys.modules['__main__'].__file__)

image_list = []
resized_images = []

ratiosList = []
namesList = []

#change the image extension accordingly if needed
modDirPath = dirPath + "/*.jpg"

for filename in natsorted(glob.glob(modDirPath)):
    print(filename)
    basename = os.path.basename(filename)
    namesList.append(os.path.splitext(basename)[0])
    img = Image.open(filename)
    ratio = img.size[1] / img.size[0]
    ratiosList.append(ratio)
    image_list.append(img)

for image in image_list:
    for i in range(len(ratiosList)):
        image = image.resize((900, int(900*ratiosList[i])))
        resized_images.append(image)
        break

new_folder = f'{dirPath}/resized_images'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for (i, new) in enumerate(resized_images):
    new.save("{}{}".format(new_folder, "/"+namesList[i]+"_resized.jpg"))




        

