# -*- coding: utf-8 -*-
# import module snippets
from ...base import Base
from .Projects import Client as Projects


class Client(Base):
    __projects: Projects = None

    @property
    def projects(self):
        if self.__projects is None:
            self.__projects = Projects(client=self)
        return self.__projects
