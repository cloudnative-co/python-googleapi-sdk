# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from .Speech import Client as Speech
from .Storage import Client as Storage
from .BigQuery import Client as BigQuery


class Client(Base):
    __speech: Speech = None
    __storage: Storage = None
    __bigquery: BigQuery = None

    @property
    def speech(self):
        if self.__speech is None:
            self.__speech = Speech(client=self)
        return self.__speech

    @property
    def storage(self):
        if self.__storage is None:
            self.__storage = Storage(client=self)
        return self.__storage

    @property
    def bigquery(self):
        if self.__bigquery is None:
            self.__bigquery = BigQuery(client=self)
        return self.__bigquery
