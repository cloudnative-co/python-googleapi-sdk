import io

from ...base import Base
from ...utilities import request_parameter


class Buckets(Base):

    def delete(
        self, bucket: str, if_metageneration_match: int = None,
        if_metageneration_not_match: int = None, projection: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, bucket: str, if_metageneration_match: int = None,
        if_metageneration_not_match: int = None, projection: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self,
        project: str, name: str,
        predefined_acl: str = None, predefined_default_object_acl: str = None,
        projection: str = None, acl: list = None, requester_pays: bool = None,
        cors: list = None, default_event_based_hold: bool = None,
        default_object_acl: list = None, default_kms_key_name: str = None,
        uniform_bucket_level_access: dict = None, labels: dict = None,
        lifecycle: dict = None, location: str = None, log_bucket: str = None,
        log_object_prefix: str = None, retention_period: dict = None,
        storage_class: str = None, versioning: bool = None,
        main_page_suffix: str = None, not_found_page: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self,
        project: str = None, max_result: int = None, page_token: str = None,
        prefix: str = None, projection: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
