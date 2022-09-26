from ....base import Base
from ....utilities import request_parameter


class ServiceAccounts(Base):

    def list(
        self, project_id: str, page_token: str = None, page_size: int = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(self, project_id: str, client_id: str) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
