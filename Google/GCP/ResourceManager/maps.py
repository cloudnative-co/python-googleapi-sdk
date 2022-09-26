Maps = {
    "Projects": {
        "list": {
            "method": "GET",
            "url": "https://cloudresourcemanager.googleapis.com/v1/projects",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/cloud-platform.read-only",
                    "https://www.googleapis.com/auth/cloudplatformprojects",
                    "https://www.googleapis.com/auth/cloudplatformprojects.readonly"
                ]
            },
            "query": """{{
                "pageSize": {page_size},
                "pageToken": {page_token},
                "filter": {filter}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://iam.googleapis.com/v1/projects/{project_id}/serviceAccounts/{client_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/iam",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            }
        }
    }
}
