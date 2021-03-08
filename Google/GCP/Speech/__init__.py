from ...base import Base
from .speech import Speech


class Client(Base):
    __speech: Speech = None

    @property
    def version(self):
        return 1

    @property
    def speech(self):
        if self.__speech is None:
            self.__speech = Speech(client=self)
        return self.__speech
