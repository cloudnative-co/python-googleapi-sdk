from ...base import Base
from .files import Files


class Client(Base):
    __files: Files = None

    @property
    def version(self):
        return 3

    @property
    def files(self):
        if self.__files is None:
            self.__files = Files(client=self)
        return self.__files
