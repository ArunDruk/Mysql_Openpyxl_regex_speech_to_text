############################################################# Image Captcha ###############################################################################
# from captcha.image import ImageCaptcha
#
# image=ImageCaptcha()
# data = image.generate("arun842")
# image.write("arun842", 'captcha1.png')
############################################################################################################################################
######################################################### Audio Captcha ###################################################################################

# from captcha.audio import AudioCaptcha
#
# audio= AudioCaptcha()
# data = audio.generate('543')  # Drawback, this is not working for alphabets, works for numerics
# audio.write("543",'captcha11.wav')
##################################################### Generating image using random alphabets and digits#######################################################################################
# import string
# import random
# from captcha.image import ImageCaptcha
#
# alpha_chars=string.ascii_letters
# numerics=string.digits
#
# nums="".join(random.choice(numerics) for i in range(4))
# alpha_bets="".join(random.choice(alpha_chars) for i in range(4))
#
# input_str=alpha_bets+nums
# image = ImageCaptcha()
# data = image.generate(input_str)
# image.write(input_str, 'captcha1.png')
############################################################################################################################################
