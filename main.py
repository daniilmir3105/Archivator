# This is a sample Python script.
import downloader_for_youtube
import make_zip
import backup_for_games

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hello, ' + name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # this is basic object for working with files and maps
    obj_for_archivating = make_zip.Zip()
    obj_for_archivating.basic_method = r'C:\Users\Daniil\Documents\УТЁБА\Инженерка'
    map_path = obj_for_archivating.basic_method
    back = backup_for_games.Backup()
    youtube_obj = downloader_for_youtube.Downloading()

    # obj_for_archivating.make_zip_archive(path_from=map_path, path_to=r'C:\Users\Daniil\Documents\Daniil', file_name='archive')
    # print_hi('world!')
    # back.make_backup(path_from=map_path, path_to=r'C:\Users\Daniil\Documents\Daniil\Backups\TLD')
    youtube_obj.basic_method = r'C:\Users\Daniil\Downloads'
    dir_path = youtube_obj.basic_method
    youtube_obj.url_function = 'https://youtu.be/ZSVoNDT4m3U'
    video_url = youtube_obj.url_function

    youtube_obj.download_video(url=video_url, path_to=dir_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# https://youtu.be/ZSVoNDT4m3U