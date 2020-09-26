from types import MethodType
from ...base import Base
from ...utilities import request_parameter


class Messages(Base):

    def list(
        self, user_id: str,
        max_results: str = None, page_token: str = None, q: str = None,
        label_ids: str = None, include_spam_trash: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, user_id: str, id: str,
        format: str = None, metadata_headers: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
