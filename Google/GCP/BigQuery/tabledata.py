from ...base import Base
from ...utilities import request_parameter


class TableData(Base):

    def insert_all(
        self, project_id: str, dataset_id: str, table_id: str,
        kind: str, template_suffix: str, rows: list, trace_id: str,
        skip_invalid_rows: bool = None, ignore_unknown_values: bool = None,
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, project_id: str, dataset_id: str, table_id: str,
        start_index: int = None, max_results: int = None,
        page_token: str = None, selected_fields: str = None,
        use_int64_timestamp: bool = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
