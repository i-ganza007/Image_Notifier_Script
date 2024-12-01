import os
import shutil
from win10toast import ToastNotifier
import datetime

today =  datetime.date.today()



toastNot = ToastNotifier()
directory = './Desktop/Useless_images'
try:
    if not os.path.exists(directory):
        os.mkdir(directory,mode=0o777,dir_fd=None)
    else:
        pass
except OSError as e:
    print(e)

# If module already exists 
def NewSystem():
    imagefiles = []
    for (root,dir,files) in os.walk('.',topdown=False):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                imagefiles.append(file)
    deleted_imgs = [image for image in imagefiles if today - os.path.getmtime(os.path.abspath( image)) > datetime.timedelta(days=7)]
    for img in deleted_imgs:
        destination_image_path = os.path.join(directory,img)
        shutil.move(os.path.abspath(img),destination_image_path)
    toastNot.show_toast(title=f'You have {len(deleted_imgs)} which are not being used for over 7 days? Delete them',duration=7)

# Add to directory if the file exists
def OldSystem():
    pass 

