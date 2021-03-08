Maps = {
    "Messages": {
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
    "Users": {
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
