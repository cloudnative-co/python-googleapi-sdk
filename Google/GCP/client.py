# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from .Speech import Client as Speech
from .BigQuery import Client as BigQuery


class Client(Base):
    __speech: Speech = None
    __bigquery: BigQuery = None

    @property
    def speech(self):
        if self.__speech is None:
            self.__speech = Speech(client=self)
        return self.__speech

    @property
    def bigquery(self):
        if self.__bigquery is None:
            self.__bigquery = BigQuery(client=self)
        return self.__bigquery
