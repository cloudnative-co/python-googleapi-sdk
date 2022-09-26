from ...base import Base
from ...utilities import request_parameter


class Projects(Base):

    def list(
        self, page_token: str = None, page_size: int = None, filter: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
