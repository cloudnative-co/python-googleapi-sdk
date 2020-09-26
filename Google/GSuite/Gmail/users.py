from ...base import Base
from ...utilities import request_parameter


class Users(Base):

    def get_profile(
        self, user_id: str
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
