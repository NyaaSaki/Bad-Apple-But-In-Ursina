
from ursina import *
import skimage
import matplotlib.pyplot as plt
from skimage.io import imread_collection



#__________________________Process Image_________________________

#your path 
col_dir = 'frames/*.png'
print("importing images")
#creating a collection with the available images
col = imread_collection(col_dir)

print("images imported")


def showImage(img):
    gs = skimage.color.rgb2gray(img)
    rs = skimage.transform.rescale(gs,0.1,anti_aliasing=False)
    #print(rs)
    for idx in range(len(rs)):
        for jdx in range(len(rs[idx])):
            if rs[idx][jdx]>0.5: rs[idx][jdx] =1
            #else: rs[idx][jdx] =0
    #print(type(rs))
    return rs


app = Ursina()

pixels = []
layout = showImage(col[0])
for idx in range(len(layout)):
    for jdx in range(len(layout[idx])):
        pixels.append(Entity(model="sphere",scale=(0.15,0.15,0.15),position = (jdx*0.2-5,3.7-idx*0.2,4),color = color.rgb(4,4,4)))
camera.position = (0,0.3,-15)
m=-1
print(len(layout))
print(len(layout[2]))
print(len(pixels))
def update():
    global m
    m+= time.dt
    print(floor(m))
    frame = showImage(col[max(floor(m*30),0)])
    for idx in range(len(layout)):
        for jdx in range(len(layout[idx])):
            alpha = frame[idx][jdx] * 255
            #print(alpha)
            #pixels[idx*len(layout[2])+jdx].z = frame[idx][jdx]*0.3
            pixels[idx*len(layout[2])+jdx].color = color.rgb(alpha,alpha,alpha)
    
    
app.run()


print("here")