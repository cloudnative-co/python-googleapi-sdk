Maps = {
    "CalendarList": {
        "list": {
            "method": "GET",
            "url": "https://www.googleapis.com/calendar/v3/users/me/calendarList",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/calendar.readonly",
                    "https://www.googleapis.com/auth/calendar"
                ]
            },
            "query": """{{
                "maxResults": {max_results},
                "minAccessRole": {min_access_role},
                "pageToken": {page_token},
                "showDeleted": {show_deleted},
                "showHidden": {show_hidden},
                "syncToken": {sync_token}
            }}"""
        }
    },
    "Events": {
        "list": {
            "method": "POST",
            "url": "https://www.googleapis.com/calendar/v3/calendars/calendar_id/events",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/calendar",
                    "https://www.googleapis.com/auth/calendar.events"
                ]
            },
            "query": """{{
                "conferenceDataVersion": {conference_data_version},
                "maxAttendees": {max_attendees},
                "sendNotifications": {send_notifications},
                "sendUpdates": {send_updates},
                "supportsAttachments": {supports_attachments}
            }}""",
            "payload": """{{
                "end": {end},
                "start": {start},
                "attachments": {attachments},
                "attendees": {attendees},
                "colorId": {color_id},
                "description": {description},
                "extendedProperties": {extended_properties},
                "gadget": {gadget},
                "guestsCanInviteOthers": {guests_can_invite_others},
                "guestsCanModify": {guests_can_modify},
                "guestsCanSeeOtherGuests": {guests_can_see_other_guests},
                "id": {id},
                "location": {location},
                "originalStartTime": {original_start_time},
                "recurrence": {recurrence},
                "reminders": {reminders},
                "sequence": {sequence},
                "source": {source},
                "status": {status},
                "summary": {summary},
                "transparency": {transparency},
                "visibility": {visibility}
            }}"""
        }
    }
}
