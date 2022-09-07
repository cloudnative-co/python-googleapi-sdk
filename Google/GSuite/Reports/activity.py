from types import MethodType
from ...base import Base
from ...utilities import request_parameter


class Activity(Base):

    def list(
        self, user_key: str = "all",
        application_name: str = "admin",
        actor_ip_address: str = None,
        customer_id: str = None,
        end_time: str = None,
        event_name: str = None,
        filters: str = None,
        max_results: str = None,
        org_unit_id: str = None,
        page_token: str = None,
        start_time: str = None,
        group_id_filter: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def watch(
        self, user_key: str = "all",
        application_name: str = "admin",
        actor_ip_address: str = None,
        customer_id: str = None,
        end_time: str = None,
        event_name: str = None,
        filters: str = None,
        max_results: str = None,
        org_unit_id: str = None,
        page_token: str = None,
        start_time: str = None,
        group_id_filter: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
