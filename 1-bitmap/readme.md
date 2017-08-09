# Exercise 1 - convert a bitmap file to grayscale

The purpose of this exercise is to help you think about binary representations of data. This will be important for later exercises, and may push you to consider questions that are lower level than your day-to-day Python programming.

Our objective in this exercise will be to write a Python program that can read a colored bitmap file and output a new bitmap file in grayscale. This may seem like a tough challenge, but we'll talk through everything you need to know to complete the exercise.

A bitmap file is fairly simple: there is some header information, then a series of bytes that represents the pixel data. There is no compression, so every three bytes represents the next pixel in order. Why three bytes? Because in a color image, we need to specify the amount of redness, greenness and blueness of each pixel. In this case (and commonly) we allow 256 levels of each of those three colors, so it takes one byte to store each color level, and 3 bytes over all.

As you will find out, the bytes are not stored in red, green and blue order... finding out the right order is part of the exercise!

You may also realize that they bytes are stored in a linear way in the file, but the image is rectangular! If we'd like to make sense of which pixels are on each row of the image (which is not actually critical for this exercise) we will need to look at the header to figure out the image width.

You will almost definitely need to know the specification of the [Bitmap file header](https://en.wikipedia.org/wiki/BMP_file_format#Bitmap_file_header) for this exercise. Reading specifications like this is a significant part of working with binary data.

But otherwise, you should have everything you need!

## Primary exercise

Write a Python program, optionally using "convert.py" as a starting point, which takes an input filename and output filename as command line arguments. It should read the input file, parse it, and compute and write back an output file that shows the image in grayscale. The grayscale algorithm can be simple, just take the average of all the color channels. If you implement the algorithm this way, you should be able to run the `./test` file to confirm that you completed the exercise correctly.

## Stretch goals

* Most humans perceive the intensity of blue and red more significantly than that of green. This makes our simple averaging algorithm a poor choice. Research the luminosity method of grayscale calculation and implement it. Try testing it on some more interesting input images and see if you agree that the luminosity weighting is a better approach
* How many passes of the input data do you do? Can you do this in a single pass?
* If we use three bytes per pixel, we are using almost 3x as much space as we really need. Do some research to determine how to output a bitmap that uses one byte per pixel, instead.
* Write a new program which can rotate a bitmap by a given amount. It will be much easier to only allow multiples of 90 deg, but a stretch stretch goal would allow for any amount.
* Write a new program that performs a Gaussian blur on the input image.
