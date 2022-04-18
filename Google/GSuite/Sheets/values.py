from ...base import Base
from ...utilities import request_parameter


class Values(Base):

    def get(
        self,
        spreadsheet_id: str,
        range: str,
        major_dimension: str = None,
        value_render_option: str = None,
        date_time_render_option: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
