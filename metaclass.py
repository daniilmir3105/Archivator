from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod

class BaseClass(metaclass=ABCMeta):
    '''
    This class will be base for our classes with methods for our app.
    '''

    # this is base field(there will be path to files or maps
    # @ab
    __path = ''

    # this will be a setter 
    @abstractmethod
    @property
    def basic_method(self):
        '''
        This abstract method will be base for other methods(*setters and getters).
        :param variable: must be string(path to file or map)
        :return: nothing 
        '''
        pass


    # this will be setter for our field 
    @abstractmethod
    @basic_method.setter
    def basic_method(self, variable):
        '''
        This abstract method will be base for other methods.
        :param variable: must be string(path to file or map)
        :return: nothing 
        '''
        self.__path = variable


    @abstractmethod
    @basic_method.getter
    def basic_method(self):
        '''
        This abstract method will get this field.
        :param: none 
        :return: field
        ''' 
        return self.__path

    @abstractmethod
    @classmethod
    def method(self, variable):
        '''
        This abstract method will be base for other methods.
        :param variable: in most situations it must path to file or map
        :return: something(new map or file, or nothing)
        '''

        pass