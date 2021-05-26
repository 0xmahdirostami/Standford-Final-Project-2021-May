from simpleimage import SimpleImage
def main():
    image=SimpleImage("mahdi.jpeg")
    for pixel in image:
        pixel.red=pixel.red//2
        pixel.green=pixel.green// 2
        pixel.blue=pixel.blue// 2
    image.show()

if __name__ == '__main__':
    main()