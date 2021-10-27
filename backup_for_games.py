from metaclass import BaseClass
# from distutils.dir_util import copy_tree
from shutil import copy, copy2, copytree

class Backup(BaseClass):
    '''
    This class will have a method for making backups for saves in my games.
    '''

    @classmethod
    def make_backup(self, path_from, path_to):
        '''
        This method will make backups for saves in my games.
        :param path_from: path of folder(string)
        :param path_to: path, where our results must be(string)
        :return: 0
        '''

        # copy_tree(src=path_from, dst=path_to)
        copytree(src=path_from, dst=path_to, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
        return 0