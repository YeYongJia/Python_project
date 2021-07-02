from PIL import Image,ImageFont,ImageDraw

def addtext(img,num):
    x,y=img.size
    img.show()
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 100)
    draw = ImageDraw.Draw(img)                        
    draw.text((x*0.8,y*0.1),str(num),font=font,fill='red')
    img.show()

ori_picture = Image.open(r'C:\Users\nicolas\Desktop\123.png')
num=4
addtext(ori_picture,num)
  


