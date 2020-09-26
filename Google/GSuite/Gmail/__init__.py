from ...base import Base
from .messages import Messages
from .users import Users


class Client(Base):
    __messages: Messages = None
    __users: Users = None

    @property
    def messages(self):
        if self.__messages is None:
            self.__messages = Messages(client=self)
        return self.__messages

    @property
    def users(self):
        if self.__users is None:
            self.__users = Users(client=self)
        return self.__users
