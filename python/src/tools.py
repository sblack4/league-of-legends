

# make a data folder 
from os import path, getcwd, mkdir


def make_data_folder(data_folder_name="data"):
    """makes a "data" folder in the current directory IF it doesn't already exist
    :param data_folder_name: if you want a name other than data
    :return: void
    """
    pwd = getcwd()
    full_path = path.join(pwd, data_folder_name)
    if not path.isdir(full_path):
        mkdir(full_path)



