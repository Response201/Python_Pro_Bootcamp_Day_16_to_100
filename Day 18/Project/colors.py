import random
import  colorgram


def random_color():
    colors = []
    for _ in range(3):
        colors.append(random.randint(20,245))

    return colors


color_from_img_array =[  (102, 164, 110),  (206, 209, 23), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149)]


#def color_from_image():
#    colors = colorgram.extract('image.jpg', 15)
#    for item in colors:
#        color_from_img_array.append((item.rgb.r, item.rgb.g,item.rgb.b ))
#
#color_from_image()


