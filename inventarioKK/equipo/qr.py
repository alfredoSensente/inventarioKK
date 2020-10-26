import qrcode
img=qrcode.make(f'https://www.youtube.com/watch?v=B4LvDiIi128')
img.show('test.png')