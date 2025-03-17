from PIL import Image

image_monro = Image.open("monro.jpg")
red_channel, green_channel, blue_channel = image_monro.split()
red_channel_middle = red_channel.crop((50, 0, 646, 522))
red_channel_left = red_channel.crop((100, 0, red_channel.width, red_channel.height))
shift_channel_red = Image.blend(red_channel_middle, red_channel_left, 0.5)
blue_channel_middle = blue_channel.crop((50, 0, 646, 522))
red_channel_right = blue_channel.crop((0, 0, 596, 522))
shift_channel_blue = Image.blend(blue_channel_middle, red_channel_right, 0.5)
green_channel_middle = green_channel.crop((50, 0, 646, 522))
image_monro_crop = Image.merge("RGB", (shift_channel_red, green_channel_middle, shift_channel_blue))
image_monro_crop.save('image_monro_crop.jpg')
image_monro_crop.thumbnail((80, 80))
image_monro_crop.save('image_monro_thumb.jpg')

