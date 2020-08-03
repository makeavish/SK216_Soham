import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from keras.models import load_model
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import matplotlib.image as mpimg
import cv2
import os
import requests

model = load_model("/Users/makeavish786/Projects/SK216_Soham/ImageVideoAnalysis/Final_weights.h5")

from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (224, 224, 3))
    np_image = np.expand_dims(np_image, axis=0)
    img=mpimg.imread(filename)
    plt.imshow(img)
    return np_image


files = os.listdir("/Users/makeavish786/Projects/SK216_Soham/ImageVideoAnalysi/images/")

while(1):
    if(len(files)!=0):
        name = "/Users/makeavish786/Projects/SK216_Soham/ImageVideoAnalysis/images/"+files[0]
        file1 = open(name,"r")
        links = set()
        check=0

        site_url = ""
        for link in file1:
            if(link=="None" or check==0):
                if check==0:
                    site_url=link
                check+=1
                continue
            else:
                links.add(link)
            

        # print(f'Site url is {site_url}. Found {len(links)} image links.')

        os.system(f'cp {name} processedImages/{files[0]}')
        os.system(f'rm -r {name}')

        total_count = len(links)
        nsfw_count = 0

        for link in links:
            with open('temp/pic1.jpg', 'wb') as handle:
                try:
                    response = requests.get(link, stream=True)
                except:
                    continue

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
            try:
                image = load("temp/pic1.jpg")
                ans = model.predict(image)
                new_ans = np.argmax(ans[0])
                if(new_ans!=0):
                    nsfw_count+=1
                os.system("rm -r temp/pic1.jpg")
            except Exception as e:
                os.system("rm -r temp/pic1.jpg")
                continue

        if(nsfw_count > 0.2 * total_count):
            os.system('echo "'+site_url+' has explicit content\n\n" >> results/result.txt')
        else:
            os.system('echo "' + site_url +' does not have explicit content\n\n"  >> results/result.txt')
    
    files = os.listdir("images")
