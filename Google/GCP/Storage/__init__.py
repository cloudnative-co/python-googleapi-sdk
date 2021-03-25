from ...base import Base
from .buckets import Buckets
from .objects import Objects
from .utility import Utility

class Client(Base):
    __buckets: Buckets = None
    __objects: Objects = None
    __utility: Utility = None


    @property
    def version(self):
        return 1

    @property
    def buckets(self) -> Buckets:
        if self.__buckets is None:
            self.__buckets = Buckets(client=self)
        return self.__buckets

    @property
    def objects(self) -> Objects:
        if self.__objects is None:
            self.__objects = Objects(client=self)
        return self.__objects

    @property
    def utility(self) -> Utility:
        if self.__utility is None:
            self.__utility = Utility(client=self)
        return self.__utility
