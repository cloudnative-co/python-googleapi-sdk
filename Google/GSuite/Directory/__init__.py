from ...base import Base
from .tokens import Tokens
from .users import Users


class Client(Base):
    __users: Users = None
    __tokens: Tokens = None

    @property
    def version(self):
        return 1

    @property
    def users(self):
        if self.__users is None:
            self.__users = Users(client=self)
        return self.__users

    @property
    def tokens(self):
        if self.__tokens is None:
            self.__tokens = Tokens(client=self)
        return self.__tokens
