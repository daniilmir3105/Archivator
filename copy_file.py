from metaclass import BaseClass
# import shutil
# import abc
import pafy

class Copying(BaseClass):
    '''
    This class will have methods to download videos from yuotube.
    '''

    # this is variable, that will have our url
    __url_var = ''

    @property
    def url_function(self):
        pass

    @url_function.setter
    def url_function(self, var):
        '''
        this is setter for __url_var
        :param var: string, url
        :return: nothing
        '''

        self.__url_var = var

    @url_function.getter
    def url_function(self):
        '''

        :return: string, __url_var
        '''

        return self.__url_var

    @classmethod
    def copy_file(self, url, path_to):
        '''

        :param url:
        :return:
        '''

        pafy_obj = pafy.new(url=url)
        pass