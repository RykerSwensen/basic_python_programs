# PIL = Python Imaging Library
# Import images.
from PIL import Image

def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage
      
image1 = Image.open("sunset.jpg")
image2 = Image.open("maxresdefault.jpg")
image3 = changeImageSize(800, 500, image1)
image4 = changeImageSize(800, 500, image2)
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")


alphaBlended1 = Image.blend(image5, image6, alpha=.2)
alphaBlended2 = Image.blend(image5, image6, alpha=.4)

alphaBlended2.show()