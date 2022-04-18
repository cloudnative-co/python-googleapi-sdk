from ...base import Base
from ...utilities import request_parameter


class SpreadSheets(Base):

    def get(
        self,
        spreadsheet_id: str,
        ranges: list = None,
        include_grid_data: bool = None,
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
