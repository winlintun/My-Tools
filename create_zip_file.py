import os
import zipfile
import datetime
import today_date_folder_created


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def strrr():
    a = str(datetime.datetime.now().date())
    return a

zip_folder = str('{}.zip'.format(strrr()))

zipf = zipfile.ZipFile(zip_folder, 'w', zipfile.ZIP_DEFLATED)

zipdir(strrr(), zipf)
input("Successfully")
zipf.close()






