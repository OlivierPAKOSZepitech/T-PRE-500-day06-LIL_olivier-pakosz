import os

DirPath = r"/home/olivierpakosz/introduction_seminar/"
result = os.walk(".", topdown=False)
for root, sous_direct, files in result:
    print(root)
    print("/////////////////////////")
    print(sous_direct)
    print("///////////////////////////")
    print(files)