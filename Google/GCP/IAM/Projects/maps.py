Maps = {
    "ServiceAccounts": {
        "list": {
            "method": "GET",
            "url": "https://iam.googleapis.com/v1/projects/{project_id}/serviceAccounts",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/iam",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "pageSize": {page_size},
                "pageToken": {page_token}
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
