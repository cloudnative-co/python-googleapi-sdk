from ...base import Base
from ...utilities import request_parameter


class Jobs(Base):

    def cancel(self, project_id: str, job_id: str, location: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(self, project_id: str, job_id: str, location: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get_query_results(
        self, project_id: str, job_id: str,
        start_index: str = None, page_token: str = None,
        max_results: int = None, timeout_ms: int = None, location: str = None,
        use_int64_timestamp: bool = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self, project_id: str, configuration: dict, job_reference: dict = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert_metadata(
        self, project_id: str, configuration: dict, job_reference: dict = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, project_id: str,
        all_users: bool = None, max_results: int = None,
        min_creation_time: str = None, max_creation_time: str = None,
        page_token: str = None, projection: str = None,
        state_filter: str = None, parent_job_id: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def query(
        self, project_id: str, kind: str, query: str,
        max_results: int = None, default_dataset_id: str = None,
        default_project_id: str = None, timeout_ms: int = None,
        dry_run: bool = None, use_query_cache: bool = None,
        use_legacy_sql: bool = None, parameter_mode: str = None,
        query_parameters: list = None, location: str = None,
        use_int64_timestamp: bool = None, connection_properties: list = None,
        labels: dict = None, maximum_bytes_billed: int = None,
        request_id: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
