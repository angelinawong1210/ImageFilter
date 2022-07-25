import image 
import statistics

#redRemover 
def redRemover(img): 
  for col in range(img.getWidth()):
    for row in range(img.getHeight()):
      p = img.getPixel(col, row)
      newpixel = image.Pixel(0, p.getGreen(), p.getBlue())
      newimg.setPixel(col, row, newpixel) 
  return newimg 

#blueRemover 
def blueRemover(img): 
  for col in range(img.getWidth()):
    for row in range(img.getHeight()):
      p = img.getPixel(col, row)
      newpixel = image.Pixel(p.getRed(), p.getGreen(), 0)
      newimg.setPixel(col, row, newpixel) 
  return newimg 


#greenRemover
def greenRemover(img): 
  for col in range(img.getWidth()):
    for row in range(img.getHeight()):
      p = img.getPixel(col, row)
      newpixel = image.Pixel(p.getRed(), 0, p.getBlue())
      newimg.setPixel(col, row, newpixel) 
  return newimg 

#smoothOut 
def smoothOut(img):
  for col in range(1, img.getWidth()-1):
    for row in range(1, img.getHeight()-1):
        p = img.getPixel(col, row)
        p1 = img.getPixel(col-1, row) 
        p2 = img.getPixel(col, row - 1) 
        p3 = img.getPixel(col+ 1, row) 
        p4 = img.getPixel(col, row + 1) 
        R = int((p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed())/4) 
        G = int((p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen())/4) 
        B = int((p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue())/4) 
        newpixel = image.Pixel(R, G, B) 
        newimg.setPixel(col, row, newpixel)
  return newimg 


#grayScale 
def grayScale(img): 
  for col in range(img.getWidth()):
      for row in range(img.getHeight()):
          p = img.getPixel(col, row)
          gray = (p.getRed() + p.getBlue() + p.getGreen())/3 
          gray = int(gray) 
          newpixel = image.Pixel(gray, gray, gray) 
          newimg.setPixel(col, row, newpixel)
  return newimg 


#noiseElimination 
def noiseElimination(img): 
  for col in range(1, img.getWidth()-1):
    for row in range(1, img.getHeight()-1):
        p = img.getPixel(col, row)
        p1 = img.getPixel(col-1, row) 
        p2 = img.getPixel(col, row - 1) 
        p3 = img.getPixel(col+ 1, row) 
        p4 = img.getPixel(col, row + 1) 
        R = int(statistics.median([p1.getRed(), p2.getRed(), p3.getRed(), p4.getRed()])) 
        G = int(statistics.median([p1.getGreen(), p2.getGreen(), p3.getGreen(), p4.getGreen()])) 
        B = int(statistics.median([p1.getBlue(), p2.getBlue(), p3.getBlue(), p4.getBlue()])) 
        newpixel = image.Pixel(R, G, B) 
        newimg.setPixel(col, row, newpixel)
  return newimg 


#addWarmth 
def addWarmth(img): 
  for col in range(img.getWidth()):
    for row in range(img.getHeight()):
      p = img.getPixel(col, row)
      R = int(p.getRed() + 20)
      if R > 255: 
        R = 255 
      newpixel = image.Pixel(R, p.getGreen(), p.getBlue())
      newimg.setPixel(col, row, newpixel) 
  return newimg 
 

#sepiaTone
def sepiaTone(img):
  grayscaleimage = image.EmptyImage(img.getWidth(), img.getHeight())
  for col in range(img.getWidth()):
      for row in range(img.getHeight()):
          p = img.getPixel(col, row)
          gray = int(0.299*p.getRed() + 0.587*p.getGreen() + 0.114*p.getBlue())
          grayscalepixel = image.Pixel(gray, gray, gray) 
          grayscaleimage.setPixel(col, row, grayscalepixel)
          
  for col in range(img.getWidth()):
      for row in range(img.getHeight()):
          p = img.getPixel(col, row)
          R = p.getRed()
          G = p.getGreen()
          B = p.getBlue()
          newR = int(R * 0.393 + G * 0.769 + B * 0.189)
          newG = int(R * 0.349 + G * 0.686 + B * 0.168)
          newB = int(R * 0.272 + G * 0.534 + B * 0.131)
          if newR > 255: 
            newR = 255 
          if newG > 255: 
            newG = 255 
          if newB > 255: 
            newB = 255 
          newpixel = image.Pixel(newR, newG, newB)
          newimg.setPixel(col, row, newpixel)               
  return newimg 


#inverted 
def inverted(img): 
  for col in range(img.getWidth()):
      for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        R = int(255 - p.getRed()) 
        B = 255 - p.getBlue() 
        G = 255 - p.getGreen()
        newpixel = image.Pixel(R, B, G) 
        newimg.setPixel(col, row, newpixel)    
  return newimg  


# Inilializing 
win = image.ImageWin()
imageURL = input("Enter the link of the picture")
img = image.Image(imageURL)
newimg = image.EmptyImage(img.getWidth(), img.getHeight())

#Type of filter 
filter = input("Which kind of filter do you want? (Enter the number only) \n 1: Red remover \n 2:Blue remover \n 3: Green remover \n 4: Smooth out \n 5: Gray scale \n 6: Noise elimination \n 7: Add Warmth \n 8: Sepia tone ")
filter = int(filter) 

if filter == 1: 
  newimg = redRemover(img)
if filter == 2: 
    newimg = blueRemover(img) 
if filter == 3: 
    newimg = greenRemover(img) 
if filter == 4: 
    newimg = smoothOut(img)
if filter == 5: 
    newimg = grayScale(img) 
if filter == 6: 
    newimg = noiseElimination(img) 
if filter == 7: 
    newimg = addWarmth(img) 
if filter == 8: 
    newimg = inverted(img)
  

newimg.draw(win)
win.exitonclick()