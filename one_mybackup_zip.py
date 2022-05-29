import os
import zipfile
from zipfile import ZipFile
from tqdm import tqdm
import time
from datetime import datetime


BASE_DIR = 'MyZip'
now = datetime.now().strftime("%d_%m_%y__%I-%M-%S-%p")


def get_all_files(folder):
    file_paths = []

    for root, directories, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def process_bar(folder):
    for _ in tqdm(range(len(get_all_files(folder)))):
        time.sleep(0.5)


def current_show():
    for i in os.listdir():
        print(i, end='\n')


def screen_cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


print("""
    1. BackUp Now
    2. Show BackUpFile
    3. Extract BackUpFile
    4. Press Enter Any Key for (exist)!!!
    """)
user = int(input("Enter Options: "))


def main():
    global user
    file_paths = get_all_files(BASE_DIR)
    backup_folder_name = BASE_DIR + str(now)
    backup_folder_name = str('{}.zip'.format(backup_folder_name))
    while user == 1 or 2 or 3:
        if user == 1:
            print("This option is automatically backup.")
            input("Press Any Key to start!!!")
            with ZipFile(backup_folder_name, 'w') as myzip:
                for files in file_paths:
                    myzip.write(files)
            print('This Folder are zipped...')
            process_bar(BASE_DIR)
            print("Done")
            print(f"Your {backup_folder_name} file are successfully zip.\n")
            current_show()
            print("""
                1. BackUp Now
                2. Show BackUpFile
                3. Extract BackUpFile
                """)
            user = int(input("Enter Options: "))
            screen_cls()
        elif user == 2:
            current_show()
            print()
            if os.path.exists(backup_folder_name):
                with ZipFile(backup_folder_name, 'r') as myzip:
                    for info in myzip.infolist():
                        print(f"Filename: {info.filename}")
                        print(f"Mod ified: {info.date_time}")
                        print(f"Normal size: {info.file_size} bytes")
                        print(f"Compressed size: {info.compress_size} bytes")
                        print("-" * 20)
                print("""
                    1. BackUp Now
                    2. Show BackUpFile
                    3. Extract BackUpFile
                    """)
                user = int(input("Enter Options: "))
            else:
                try:
                    user = input('Enter file name(.zip): ')
                    with ZipFile(user, 'r') as myzip:
                        for info in myzip.infolist():
                            print(f"Filename: {info.filename}")
                            print(f"Modified: {info.date_time}")
                            print(f"Normal size: {info.file_size} bytes")
                            print(f"Compressed size: {info.compress_size} bytes")
                            print("-" * 20)
                    print()
                    print("""
                        1. BackUp Now
                        2. Show BackUpFile
                        3. Extract BackUpFile
                        """)
                    user = int(input("Enter Options: "))
                except (Exception, FileNotFoundError, zipfile.BadZipfile) as e:
                    print(e)
        elif user == 3:
            current_show()
            print()
            try:
                backup_folder_name = input('Enter file name(.zip): ')
                print(backup_folder_name)
                with ZipFile(backup_folder_name, 'r') as myzip:
                    myzip.printdir()
                    print(f'{user} are extracting......')
                    myzip.extractall(path="C:\\Users\\wwwic\\OneDrive\\Desktop\\")
                    process_bar(backup_folder_name)
                    print("Done!")
                    exit()
            except (Exception, FileNotFoundError, zipfile.BadZipfile) as e:
                print(e)
        else:
            print("\n Program existing.....")
            exit()


if __name__ == '__main__':
    main()
