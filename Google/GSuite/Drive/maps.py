Maps = {
    "Files": {
        "list": {
            "method": "GET",
            "url": "https://www.googleapis.com/drive/v3/files",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/drive",
                    "https://www.googleapis.com/auth/drive.file",
                    "https://www.googleapis.com/auth/drive.readonly",
                    "https://www.googleapis.com/auth/drive.metadata.readonly",
                    "https://www.googleapis.com/auth/drive.appdata",
                    "https://www.googleapis.com/auth/drive.metadata",
                    "https://www.googleapis.com/auth/drive.photos.readonly"
                ]
            },
            "query": """{{
                "corpora": {corpora},
                "driveId": {drive_id},
                "fields": {fields},
                "includeItemsFromAllDrives": {include_items_from_all_drives},
                "includeLabels": {include_labels},
                "includePermissionsForView": {include_permissions_for_view},
                "orderBy": {order_by},
                "pageSize": {page_size},
                "pageToken": {page_token},
                "q": {q},
                "spaces": {spaces},
                "supportsAllDrives": {supports_all_drives}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://www.googleapis.com/drive/v3/files/{file_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/drive",
                    "https://www.googleapis.com/auth/drive.file",
                    "https://www.googleapis.com/auth/drive.readonly",
                    "https://www.googleapis.com/auth/drive.metadata.readonly",
                    "https://www.googleapis.com/auth/drive.appdata",
                    "https://www.googleapis.com/auth/drive.metadata",
                    "https://www.googleapis.com/auth/drive.photos.readonly"
                ]
            },
            "query": """{{
                "fields": {fields},
                "includeLabels": {include_labels},
                "includePermissionsForView": {include_permissions_for_view},
                "supportsAllDrives": {supports_all_drives}
            }}"""
        }
    }
}
