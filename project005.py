# iphone5 分辨率为1136*640,压缩文件夹中过大的图片，使其分辨率不大于iphone5分辨率。
import os,re
from  PIL import Image
iphone5_width=1136.0
iphone5_depth=640.0
pic_path='E:\python_project\image\\'
list = os.listdir(pic_path)
#print(list)
count = 0
for pic_name in list:
    path = pic_path + pic_name
    image = Image.open(path)
#   image.show()
    width,depth = image.size
    w_ratio = iphone5_width/width
    d_ratio = iphone5_depth/depth
#   print( w_ratio, d_ratio)
    if (w_ratio<1)|(d_ratio<1):
        count += 1
        ratio = min(w_ratio,d_ratio)
        img_out = image.resize((int(width*ratio),int(depth*ratio)),Image.ANTIALIAS)
        new_pic=re.sub(pic_name[:-4],pic_name[:-4]+'_new',pic_name)
        #print new_pic
        new_path=pic_path+new_pic
        img_out.save(new_path)
        img_out.show()
print(str(count)+ ' pictures have been changed')

        

       


    
