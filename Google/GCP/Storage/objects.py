import datetime
import io
from ...base import Base
from ...utilities import request_parameter


class Objects(Base):

    def delete(
        self, bucket: str, name: str, generation: int = None,
        if_generation_match: int = None, if_generation_not_match: int = None,
        if_metageneration_match: int = None,
        if_metageneration_not_match: int = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, bucket: str, name: str, alt: str = None, generation: int = None,
        if_generation_match: int = None, if_generation_not_match: int = None,
        if_metageneration_match: int = None,
        if_metageneration_not_match: int = None, projection: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self, bucket: str, name: str, upload_type: str,
        content_encoding: str = None, if_generation_match: int = None,
        if_generation_not_match: int = None,
        if_metageneration_match: int = None,
        if_metageneration_not_match: int = None,
        kms_key_name: str = None, predefined_acl: str = None,
        projection: str = None, acl: list = None, cache_control: str = None,
        content_disposition: str = None, content_language: str = None,
        content_type: str = None, crc32c: str = None,
        custom_time: datetime.datetime = None, event_based_hold: bool = None,
        md5_hash: str = None, metadata: dict = None,
        storage_class: str = None, temporary_hold: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, bucket: str, delimiter: str = None, end_offset: str = None,
        include_trailing_delimiter: bool = None, max_result: int = None,
        page_token: str = None, prefix: str = None, projection: str = None,
        start_offset: str = None, versions: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

