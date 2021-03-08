from ...base import Base
from ...utilities import request_parameter


class Projects(Base):

    def service_account(self, project_id: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(self, max_results: int = None, page_token: str = None):
        request = request_parameter(locals())
        return self.http_request(**request)
