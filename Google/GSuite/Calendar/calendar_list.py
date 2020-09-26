from ...base import Base
from ...utilities import request_parameter


class CalendarList(Base):

    def list(
        self,
        max_results: int = None,
        min_access_role: str = None,
        page_token: str = None,
        show_deleted: bool = None,
        show_hidden: bool = None,
        sync_token: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
