# from abc import ABC # abstract base classes

# from collections.abc import MutableSequence

# # da um erro TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
# # pois a classe mãe exige que a filha tenha certos metodos 
# class Playlist(MutableSequence):
#     pass

# filmes = Playlist()


#usando @abstractmethod garantimos que as subclasse tem que implementar esse método
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass