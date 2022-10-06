from types import MethodType
from ...base import Base
from ...utilities import request_parameter


class Tokens(Base):

    def list(self, user_key: str) -> dict:
        """
        Returns the set of tokens specified user has issued to 3rd party applications.
        Args:
            user_key str: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
        """
        request = request_parameter(locals())
        return self.http_request(**request)
