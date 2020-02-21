from PIL import Image, ImageDraw

img = Image.open("tmp.jpg")
draw = ImageDraw.Draw(img)
w, h = img.size
pix = img.load()
factor = 10
print(899)
for i in range(w):
	for j in range(h):
		a,b,c = pix[i, j]
		S = a+b+c
		if (S> (((255+factor)//2)* 3)):
			a, b, c = 255, 255, 255
		else:
			a, b, c = 0, 0, 0
		draw.point((i,j),(a,b,c))
img.save("new.jpg", "JPEG")
del(draw)