from ...base import Base
from ...utilities import request_parameter


class DataSets(Base):

    def get(self, project_id: str, dataset_id: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, project_id: str,
        max_results: int = None, page_token: str = None, all: bool = None,
        filter: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self, project_id: str,
        reference_dataset_id: str, reference_project_id: str,
        friendly_name: str = None, description: str = None,
        default_table_expiration_ms: str = None,
        default_partition_expiration_ms: str = None,
        labels: dict = None, access: list = None, creation_time: str = None,
        last_modified_time: str = None, location: str = None,
        kms_key_name: str = None, satisfies_pzs: bool = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def delete(
        self, project_id: str, dataset_id: str,
        delete_contents: bool = False
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def patch(
        self, project_id: str, dataset_id: str,
        reference_dataset_id: str, reference_project_id: str,
        friendly_name: str = None, description: str = None,
        default_table_expiration_ms: str = None,
        default_partition_expiration_ms: str = None,
        labels: dict = None, access: list = None, creation_time: str = None,
        last_modified_time: str = None, location: str = None,
        kms_key_name: str = None, satisfies_pzs: bool = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def update(
        self, project_id: str, dataset_id: str,
        reference_dataset_id: str, reference_project_id: str,
        friendly_name: str = None, description: str = None,
        default_table_expiration_ms: str = None,
        default_partition_expiration_ms: str = None,
        labels: dict = None, access: list = None, creation_time: str = None,
        last_modified_time: str = None, location: str = None,
        kms_key_name: str = None, satisfies_pzs: bool = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)
