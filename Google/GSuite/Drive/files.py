from ...base import Base
from ...utilities import request_parameter


class Files(Base):

    def list(
        self,
        corpora: str = None, drive_id: str = None, fields: str = None,
        include_items_from_all_drives: bool = None,
        include_labels: str = None,
        include_permissions_for_view: str = None, order_by: str = None,
        page_size: int = None, page_token: str = None, q: str = None,
        spaces: str = None, supports_all_drives: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self,
        file_id: str,
        acknowledge_abuse: bool = None,
        fields: str = None,
        include_labels: str = None,
        include_permissions_for_view: str = None,
        supports_all_drives: bool = None
    ) -> dict:
        """
        Gets a file's metadata or content by ID.
        Args:
            fileId   string  The ID of the file.
            acknowledgeAbuse    boolean Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media. (Default: false)
            fields  string  The paths of the fields you want included in the response. If not specified, the response includes a default set of fields specific to this method. For development you can use the special value * to return all fields, but you'll achieve greater performance by only selecting the fields you need. For more information, see Return specific fields for a file.
            includeLabels   string  A comma-separated list of IDs of labels to include in the labelInfo part of the response.
            includePermissionsForView   string  Specifies which additional view's permissions to include in the response. Only 'published' is supported.
            supportsAllDrives   boolean Whether the requesting application supports both My Drives and shared drives. (Default: false)
        """
        request = request_parameter(locals())
        return self.http_request(**request)
