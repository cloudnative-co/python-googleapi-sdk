from ....base import Base
from .service_accounts import ServiceAccounts


class Client(Base):
    __service_accounts: ServiceAccounts = None

    @property
    def version(self):
        return 1

    @property
    def service_accounts(self):
        if self.__service_accounts is None:
            self.__service_accounts = ServiceAccounts(client=self)
        return self.__service_accounts
