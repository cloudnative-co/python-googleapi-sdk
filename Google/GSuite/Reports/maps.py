Maps = {
    "Activity": {
        "list": {
            "method": "GET",
            "url": "https://admin.googleapis.com/admin/reports/v1/activity/users/{user_key}/applications/{application_name}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.reports.audit.readonly"
                ]
            },
            "query": """{{
                "actorIpAddress": {actor_ip_address},
                "customerId": {customer_id},
                "endTime": {end_time},
                "eventName": {event_name},
                "filters": {filters},
                "maxResults": {max_results},
                "orgUnitId": {org_unit_id},
                "startTime": {start_time},
                "groupIdFilter": {group_id_filter},
                "pageToken": {page_token}
            }}"""
        },
        "watch": {
            "method": "POST",
            "url": "https://admin.googleapis.com/admin/reports/v1/activity/users/{user_key}/applications/{application_name}/watch",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.reports.audit.readonly"
                ]
            },
            "query": """{{
                "actorIpAddress": {actor_ip_address},
                "customerId": {customer_id},
                "endTime": {end_time},
                "eventName": {event_name},
                "filters": {filters},
                "maxResults": {max_results},
                "orgUnitId": {org_unit_id},
                "startTime": {start_time},
                "groupIdFilter": {group_id_filter},
                "pageToken": {page_token}
            }}"""
        }
    }
}
