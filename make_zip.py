# import metaclass as mc
from metaclass import BaseClass
import shutil
# from abc import abstractmethod, abstractproperty

# Base = mc.BaseClass()

class Zip(BaseClass):
    '''
    This class will have fields and methods, that will make zip-archives.
    '''

    @classmethod
    def make_zip_archive(self, path_from, path_to, file_name):
        '''
        This method will have
        :param path_from: string(path of files and maps, that must be archived)
        path_to: string(path to files and maps)
        file_name: string(name of zip-archive)
        :return: none
        '''

        shutil.make_archive(base_name=path_to + '/' + file_name, format='zip', root_dir=path_from)
        # return 0
        pass