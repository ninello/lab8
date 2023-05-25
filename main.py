def num1():
    from PIL import Image
    im = Image.open("postcard.jpg")
    im_crop = im.crop((110, 210, 640, 470))
    im_crop.save('cropped_postcard.jpg')

def num2():
    from PIL import Image
    d = {1: "postcard.jpg", 2: "23f.jpg", 3: "dr.jpg", 4: "8m.jpg"}
    print(" 1 - Новый год"
          " 2 - 23 Февраля"
          " 3 - День рождения"
          " 4 - 8 Марта")
    card = int(input("Введите номер нужной открытки: "))
    filename = d[card]
    with Image.open(filename) as img:
        img.load()
        img.show()

def num3():
    from PIL import Image, ImageDraw, ImageFont

    im = Image.open("postcard.jpg")

    font = ImageFont.truetype('arial.ttf', 25)
    drawer = ImageDraw.Draw(im)
    ask = input("Введите имя принимающего")
    drawer.text((10, 10), ask, "-", "поздравляем", font=font, fill="black")

    im.save('new_postcard.jpg')
    im.show()


