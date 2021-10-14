import metaclass as mc
# from abc import abstractmethod, abstractproperty

Base = mc.BaseClass()

class Zip(Base):
    '''
    This class will have fields and methods, that will make zip-archives.
    '''

    __map_path = '' 

    # this is setter for our map-path
    def set_map_path(self, var): #-> Base.set_field()
        self.__map_path = var

    # this is getter for our map-path
    def get_map_path(self): #-> Base.set_field()
        return self.__map_path
        # pass