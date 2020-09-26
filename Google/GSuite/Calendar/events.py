from ...base import Base
from ...utilities import request_parameter


class Events(Base):

    def insert(
        self,
        calendar_id: str,
        start: dict, end: dict,
        anyone_can_add_self: bool = None, attachments: list = None,
        attendees: list = None, color_id: str = None,
        conference_data: dict = None, description: str = None,
        extended_properties: dict = None, gadget: dict = None,
        guests_can_invite_others: boolean = None,
        guests_can_modify: boolean = None,
        guests_can_see_other_guests: boolean = None,
        id: str = None, location: str = None, original_start_time: dict = None,
        recurrence: list = None, reminders: dict = None, sequence: int = None
        source: dict = None, status: str = None, summary: str = None,
        transparency: str = None, visibility: str = None,
        conference_data_version: int = None,
        max_attendees: int = None, send_notifications: bool = None,
        send_updates: str = None, supports_attachments: bool = None,
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
