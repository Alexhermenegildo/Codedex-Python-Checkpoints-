import imageio.v3 as iio

filenames = ['picture1.png', 'picture2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
  
iio.imwrite('luffy.gif', images, duration = 500, loop = 0)
  
  