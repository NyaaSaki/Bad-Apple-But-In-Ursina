
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
            else: rs[idx][jdx] =0
    #print(type(rs))
    return rs


app = Ursina()
cube = Entity(model = "cube",color = color.rgb(200,150,200),texture="white_cube")
urFloor = Entity(model = 'cube',color = color.rgb(30,50,30),scale = (40,1,40), position = (0,-2.5,0))

txt = Text(text="tree")
treelog = Entity(model = "cube",position = (3,0,5), scale = (1,3,1), color = color.rgb(15,5,10),texture="white_cube")
treeleaf = Entity(model = 'cube',color = color.rgb(80,100,80),scale = (3,3,3), position = (3,2,5),texture="white_cube")
m= 0 

def update():
    global m
    m+=1
    cube.y -= time.dt*0.5
    cube.color = color.rgb(m%255,5,5)
    if cube.y < -2:
        cube.y = 0
    camera.position = ((m%200 - 100) / 100,0,-20)
    
    
app.run()


print("here")