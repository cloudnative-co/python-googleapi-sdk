from ...base import Base
from .spreadsheets import SpreadSheets
from .values import Values


class Client(Base):
    __spreadsheets: SpreadSheets = None
    __values: Values = None

    @property
    def version(self):
        return 4

    @property
    def spreadsheets(self):
        if self.__spreadsheets is None:
            self.__spreadsheets = SpreadSheets(client=self)
        return self.__spreadsheets

    @property
    def values(self):
        if self.__values is None:
            self.__values = Values(client=self)
        return self.__values
