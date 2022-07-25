# ImageFilter
This is our project at TechGirls 2022, Virginia Tech under the guidance of Dr. Onyeka Emebo

## Functions

Our project consists of 8 main functions, which are equivalent to 8 filters for the images:

- redRemover: Remove the red color of the images

Set the red parameter in the RGB code into 0

- blueRemover: Remove the blue color of the images

Set the blue parameter in the RGB code into 0

- greenRemover: Remove the green color of the images

Set the green parameter in the RGB code into 0

- smoothOut: Smooth out the images

Replace each pixel with the average values of the pixels around it

- noiseElimination: Eliminate the noise in the images

Replace each pixel by the median value of the pixels surrounding it

- addWarmth: Add more warmth to the images

Increase the red parameter of the RGB code  

- sepiaTone: Convert the images into the Sepia Tone

Using these following function to adjust the parameters

newR = (R × 0.393 + G × 0.769 + B × 0.189)

newG = (R × 0.349 + G × 0.686 + B × 0.168)

newB = (R × 0.272 + G × 0.534 + B × 0.131)

- grayScale: Convert the images into the Gray scale images

Use the luminosity method: val = 0.21 R + 0.72 G + 0.07 B

## Instruction: 

- Execute the file image.py first 

- Execute the file main.py 

- Enter the image link (we provide you with one image sample.jpg) 

- Enter the number of the filter you want to apply -> DONE! 
