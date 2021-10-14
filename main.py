# This is a sample Python script.
import make_zip

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hello, ' + name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # this is basic object for working with files and maps
    obj_for_archivating = make_zip.Zip()
    obj_for_archivating.basic_method = r'C:\Users\Daniil\Documents\BioWare'
    map_path = obj_for_archivating.basic_method

    obj_for_archivating.make_zip_archive(path_from=map_path, path_to=r'', file_name='archive')
    # print_hi('world!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
