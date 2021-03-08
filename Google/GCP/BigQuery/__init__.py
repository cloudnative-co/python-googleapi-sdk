from ...base import Base
from .datasets import DataSets
from .jobs import Jobs
from .projects import Projects
from .tabledata import TableData
from .tables import Tables


class Client(Base):
    __datasets: DataSets = None
    __jobs: Jobs = None
    __projects: Projects = None
    __tabledata: TableData = None
    __tables: Tables = None

    @property
    def version(self):
        return 2

    @property
    def datasets(self):
        if self.__datasets is None:
            self.__datasets = DataSets(client=self)
        return self.__datasets

    @property
    def jobs(self):
        if self.__jobs is None:
            self.__jobs = Jobs(client=self)
        return self.__jobs

    @property
    def projects(self):
        if self.__projects is None:
            self.__projects = Projects(client=self)
        return self.__projects

    @property
    def tabledata(self):
        if self.__tabledata is None:
            self.__tabledata = TableData(client=self)
        return self.__tabledata

    @property
    def tables(self):
        if self.__tables is None:
            self.__tables = Tables(client=self)
        return self.__tables
