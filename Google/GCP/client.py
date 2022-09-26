# -*- coding: utf-8 -*-
# import module snippets
from ..base import Base
from .BigQuery import Client as BigQuery
from .IAM import Client as IAM
from .Speech import Client as Speech
from .Storage import Client as Storage
from .ResourceManager import Client as ResourceManager



class Client(Base):
    __bigquery: BigQuery = None
    __iam: IAM = None
    __speech: Speech = None
    __storage: Storage = None
    __resource_manager: ResourceManager = None

    @property
    def bigquery(self):
        if self.__bigquery is None:
            self.__bigquery = BigQuery(client=self)
        return self.__bigquery

    @property
    def iam(self):
        if self.__iam is None:
            self.__iam = IAM(client=self)
        return self.__iam

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
    def resource_manager(self):
        if self.__resource_manager is None:
            self.__resource_manager = ResourceManager(client=self)
        return self.__resource_manager
