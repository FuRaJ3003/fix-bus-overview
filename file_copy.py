# Quick generator for filling gallery-page
import shutil
import os

# base file
base_dir = r'C:\Users\FuRaJ\Desktop\FIX-BUS - Slide test\img\base.jpg'

# path to copying folder
c_dir = r'C:\Users\FuRaJ\Desktop\FIX-BUS - Slide test\img\galery_images'

# path of copied file to rename
c_dir_copied = r'C:\Users\FuRaJ\Desktop\FIX-BUS - Slide test\img\galery_images\base.jpg'

for x in range(10):
    shutil.copy(base_dir, c_dir)
    new_number = 'C:\\Users\\FuRaJ\\Desktop\\FIX-BUS - Slide test\\img\\galery_images\\' + str(x+1) + ".jpg"
    os.rename(c_dir_copied, new_number)

