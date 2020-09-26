Maps = {
    "Google.GSuite.Calendar.calendar_list.CalendarList": {
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
    "Google.GSuite.Calendar.events.Events": {
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
    },
    "Google.GSuite.Directory.users.Users": {
        "list": {
            "method": "GET",
            "url": "https://www.googleapis.com/admin/directory/v1/users",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user.readonly",
                    "https://www.googleapis.com/auth/admin.directory.user",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "customFieldMask": {custom_field_mask},
                "customer": {customer},
                "domain": {domain},
                "maxResults": {max_results},
                "orderBy": {order_by},
                "pageToken": {page_token},
                "projection": {projection},
                "query": {query},
                "showDeleted": {show_deleted},
                "sortOrder": {sort_order},
                "viewType": {view_type}
            }}"""
        }
    },
    "Google.GSuite.Gmail.messages.Messages": {
        "get": {
            "method": "GET",
            "url": "https://gmail.googleapis.com/gmail/v1/users/{user_id}/messages/{id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://mail.google.com/",
                    "https://www.googleapis.com/auth/gmail.modify",
                    "https://www.googleapis.com/auth/gmail.readonly",
                    "https://www.googleapis.com/auth/gmail.addons.current.message.metadata",
                    "https://www.googleapis.com/auth/gmail.addons.current.message.readonly",
                    "https://www.googleapis.com/auth/gmail.addons.current.message.action"
                ]
            },
            "query": """{{
                "format": {format},
                "metadataHeaders": {metadata_headers}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://gmail.googleapis.com/gmail/v1/users/{user_id}/messages",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://mail.google.com/",
                    "https://www.googleapis.com/auth/gmail.modify",
                    "https://www.googleapis.com/auth/gmail.readonly"
                ]
            },
            "query": """{{
                "maxResults": {max_results},
                "pageToken": {page_token},
                "q": {q},
                "labelIds": {label_ids},
                "includeSpamTrash": {include_spam_trash}
            }}"""
        }
    },
    "Google.GSuite.Gmail.users.Users": {
        "get_profile": {
            "method": "GET",
            "url": "https://gmail.googleapis.com/gmail/v1/users/{user_id}/profile",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://mail.google.com/",
                    "https://www.googleapis.com/auth/gmail.modify",
                    "https://www.googleapis.com/auth/gmail.compose",
                    "https://www.googleapis.com/auth/gmail.readonly",
                    "https://www.googleapis.com/auth/gmail.metadata"
                ]
            }
        }
    }
}
