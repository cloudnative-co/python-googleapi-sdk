from ...base import Base
from ...utilities import request_parameter


class Tables(Base):

    def delete(
        self, project_id: str, dataset_id: str, table_id: str,
        selected_fields: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, project_id: str, dataset_id: str, table_id: str,
        selected_fields: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get_iam_policy(
        self, project_id: str, dataset_id: str, table_id: str,
        requested_policy_version: int = 0
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self,
        project_id: str,
        dataset_id: str,
        schema_fields: list,
        reference_dataset_id: str = None, reference_project_id: str = None,
        reference_table_id: str = None,
        time_partitioning_type: str = None, time_partitioning_expiration_ms: str = None,
        time_partitioning_field: str = None,
        time_partitioning_require_partition_filter: bool = None,
        range_partitioning_field: str = None, range_partitioning_start: str = None,
        range_partitioning_end: str = None, range_partitioning_interval: str = None,
        clustering_fields: list = None,
        friendly_name: str = None, description: str = None,
        labels: dict = None, require_partition_filter: bool = None,
        expiration_time: str = None, view: dict = None,
        external_data_configuration = None, kms_key_name: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, project_id: str, dataset_id: str,
        max_results: int = None, page_token: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def patch(
        self, project_id: str, dataset_id: str, table_id: str,
        reference_dataset_id: str, reference_project_id: str,
        reference_table_id: str, schema_fields: list,
        time_partitioning_type: str, time_partitioning_expiration_ms: str,
        time_partitioning_field: str,
        time_partitioning_require_partition_filter: bool,
        range_partitioning_field: str, range_partitioning_start: str,
        range_partitioning_end: str, range_partitioning_interval: str,
        clustering_fields: list,
        friendly_name: str = None, description: str = None,
        labels: dict = None, require_partition_filter: bool = None,
        expiration_time: str = None, view: dict = None,
        external_data_configuration = None, kms_key_name: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def set_iam_policy(
        self, project_id: str, dataset_id: str, table_id: str,
        policy: dict, update_mask: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def test_iam_policy(
        self,
        project_id: str, dataset_id: str, table_id: str, permissions: list
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def update(
        self, project_id: str, dataset_id: str, table_id: str,
        reference_dataset_id: str, reference_project_id: str,
        reference_table_id: str, schema_fields: list,
        time_partitioning_type: str, time_partitioning_expiration_ms: str,
        time_partitioning_field: str,
        time_partitioning_require_partition_filter: bool,
        range_partitioning_field: str, range_partitioning_start: str,
        range_partitioning_end: str, range_partitioning_interval: str,
        clustering_fields: list,
        friendly_name: str = None, description: str = None,
        labels: dict = None, require_partition_filter: bool = None,
        expiration_time: str = None, view: dict = None,
        external_data_configuration = None, kms_key_name: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
