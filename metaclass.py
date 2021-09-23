from abc import ABCMeta, abstractmethod, abstractproperty

class BaseClass(metaclass=ABCMeta):
    '''
    This class will be base for our classes with methods for our app.
    '''

    # this is base field(there will be path to files or maps
    __field = ''

    # this will be

    @abstractmethod
    def method(self, variable):
        '''
        This abstract method will be base for other methods.
        :param variable: in most situations it must path to file or map
        :return: something(new map or file, or nothing)
        '''

        pass