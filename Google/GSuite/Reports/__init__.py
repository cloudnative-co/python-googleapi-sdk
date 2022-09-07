from ...base import Base
from .activity import Activity


class Client(Base):
    """
    @brief          Reports API
    @details        Admin SDKは、企業ドメインの管理者が、ユーザーやグループなどのリソースを表示・管理することを可能にします。また、ドメインの監査と使用状況のレポートも提供します。
    """
    __activity: Activity = None

    @property
    def version(self):
        return 1

    @property
    def activity(self):
        if self.__activity is None:
            self.__activity = Activity(client=self)
        return self.__activity
