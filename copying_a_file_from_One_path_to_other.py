import os
from shutil import copy

# print(os.getcwd())
source_path= "C:\Arun\Personal\Source_folder"
dest_path= "C:\Arun\Dest_folder"
file_name="CoStar_GL_CAI_US_2019.txt"
#
# os.chdir(source_path)
# print(os.getcwd())
#
# if os.path.exists(file_name):
#     print(f"File found {file_name} in {source_path}")
#
#     os.chdir(dest_path)
#     if os.path.exists(file_name):
#         os.remove(file_name)
#         print(f"File already present in '{dest_path}' deleting it")
#
#     print(f"Copying the file to '{dest_path}'")
#     copy(source_path+'\\'+file_name,dest_path)  # shutil.copy(src_with_filename, dest)
#
# else:
#     print(f"File Not found in {source_path}")


################################# Checking whether the path is file or a folder ##############################
print(os.path.isfile(file_name))
print(os.path.isdir(dest_path))