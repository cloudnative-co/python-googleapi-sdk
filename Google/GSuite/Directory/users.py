from types import MethodType
from ...base import Base
from ...utilities import request_parameter


class Users(Base):

    def list(
        self,
        custom_field_mask: str = None, customer: str = None,
        domain: str = None, max_results: int = None, order_by: str = None,
        page_token: str = None, projection: str = None, query: str = None,
        show_deleted: str = None, sort_order: str = None, view_type: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
