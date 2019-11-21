# Counting objects
In this we’ll learn how to use create a simple Python + OpenCV script to count the number of Tetris blocks in the tetris image  
**Along the way we’ll be:**  
- Learning how to convert images to grayscale with OpenCV
- Performing edge detection
- Thresholding a grayscale image
- Finding, counting, and drawing contours
- Conducting erosion and dilation
- Masking an image

**We provide three parameters to the cv2.Canny  function:**
- img : The gray  image.
- minVal : A minimum threshold, in our case 30 .
- maxVal : The maximum threshold which is 150  in our example.

**Thresholding** can be used to remove lighter or darker regions and contours of images.
- Grabbing all pixels in the gray  image greater than 225 and setting them to 0 (black) which corresponds to the background of the image
- Setting pixel vales less than 225 to 255 (white) which corresponds to the foreground of the image (i.e., the Tetris blocks themselves).

**Detecting and drawing contours**
we use cv2.findContours  to detect the contours in the image. our algorithm is finding all foreground (white) pixels in the threshold.copy()  image  
we draw each **cnt**  from the **contours**  list on the image using the appropriately named **cv2.drawContours** . I am using black color which is represented by the tuple (0, 0, 0)

**Erosions and dilations**
Erosions and dilations are typically used to reduce noise in binary images   
- To reduce the size of foreground objects we can erode away pixels given a number of iterations
- To enlarge the size of foreground objects we can dilate away pixels given a number of iterations

**Masking and bitwise operations**
- “masks” will hide regions of images we do not care about.

**commands to run**
- python tetris.py -i tetris.png
- python tetris.py -i tetris2.png
- python tetris.py -i tetris3.bmp