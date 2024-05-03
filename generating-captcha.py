# pip install captcha
from captcha.image import ImageCaptcha

# Configura a imagem
image = ImageCaptcha(width=280, heigth=90)

# Texto escolhido para o captcha
captcha_text = 'MakiGehon'

# Gera a imagem do captcha
data = image.generate(captcha_text)

# Salva a imagem no caminho escolhido
image.write(captcha_text, 'captcha.png')