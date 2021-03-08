from ...base import Base
from .users import Users


class Client(Base):
    __users: Users = None

    @property
    def version(self):
        return 1

    @property
    def users(self):
        if self.__users is None:
            self.__users = Users(client=self)
        return self.__users
