# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from .Calendar import Client as Calendar
from .Directory import Client as Directory
from .Gmail import Client as Gmail
from .Sheets import Client as Sheets


class Client(Base):
    __calendar: Calendar = None
    __directory: Directory = None
    __gmail: Gmail = None
    __sheets: Sheets = None

    @property
    def calendar(self):
        if self.__calendar is None:
            self.__calendar = Calendar(client=self)
        return self.__calendar

    @property
    def directory(self):
        if self.__directory is None:
            self.__directory = Directory(client=self)
        return self.__directory

    @property
    def gmail(self):
        if self.__gmail is None:
            self.__gmail = Gmail(client=self)
        return self.__gmail

    @property
    def sheets(self):
        if self.__sheets is None:
            self.__sheets = Sheets(client=self)
        return self.__sheets
