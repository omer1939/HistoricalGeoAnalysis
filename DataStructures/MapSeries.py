from abc import ABC, abstractmethod, abstractproperty

class Map:

    #TODO write me
    pass


class MapSeries(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self, item)->Map:
        pass

    @abstractmethod
    def __len__(self):
        pass