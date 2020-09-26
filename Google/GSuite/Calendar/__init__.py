from ...base import Base
from .calendar_list import CalendarList


class Client(Base):
    __calendar_list: CalendarList = None

    @property
    def calendar_list(self):
        if self.__calendar_list is None:
            self.__calendar_list = CalendarList(client=self)
        return self.__calendar_list
