Maps = {
    "Users": {
        "delete": {
            "method": "DELETE",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user",
                ]
            }
        },
        "get": {
            "method": "GET",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user",
                    "https://www.googleapis.com/auth/admin.directory.user.readonly"
                ]
            },
            "query": """{{
                "customFieldMask": {custom_field_mask},
                "projection": {projection},
                "viewType": {view_type}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://www.googleapis.com/admin/directory/v1/users",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user"
                ]
            },
            "payload": """{{
                "id": {id},
                "primaryEmail": {primary_email},
                "password": {password},
                "hashFunction": {hash_function},
                "suspended": {suspended},
                "changePasswordAtNextLogin": {change_password_at_next_login},
                "ipWhitelisted": {ip_whitelisted},
                "name": {{
                    "familyName": {family_name},
                    "givenName": {given_name}
                }},
                "emails": {emails},
                "externalIds": {external_ids},
                "relations": {relations},
                "addresses": {addresses},
                "organizations": {organizations},
                "phones": {phones},
                "languages": {languages},
                "posixAccounts": {posix_accounts},
                "sshPublicKeys": {ssh_public_keys},
                "notes": {notes},
                "websites": {websites},
                "locations": {locations},
                "includeInGlobalAddressList": {include_in_global_address_list},
                "keywords": {keywords},
                "gender": {gender},
                "ims": {ims},
                "customSchemas": {custom_schemas},
                "archived": {archived},
                "orgUnitPath": {org_unit_path},
                "recoveryEmail": {recovery_email},
                "recoveryPhone": {recovery_phone}
            }}"""
        },
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
        },
        "make_admin": {
            "method": "POST",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}/makeAdmin",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user"
                ]
            },
            "payload": """{{
                "status": {status}
            }}"""
        },
        "patch": {
            "method": "PATCH",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user"
                ]
            },
            "payload": """{{
                "id": {id},
                "primaryEmail": {primary_email},
                "password": {password},
                "hashFunction": {hash_function},
                "suspended": {suspended},
                "changePasswordAtNextLogin": {change_password_at_next_login},
                "ipWhitelisted": {ip_whitelisted},
                "name": {{
                    "familyName": {family_name},
                    "givenName": {given_name}
                }},
                "emails": {emails},
                "externalIds": {external_ids},
                "relations": {relations},
                "addresses": {addresses},
                "organizations": {organizations},
                "phones": {phones},
                "languages": {languages},
                "posixAccounts": {posix_accounts},
                "sshPublicKeys": {ssh_public_keys},
                "notes": {notes},
                "websites": {websites},
                "locations": {locations},
                "includeInGlobalAddressList": {include_in_global_address_list},
                "keywords": {keywords},
                "gender": {gender},
                "ims": {ims},
                "customSchemas": {custom_schemas},
                "archived": {archived},
                "orgUnitPath": {org_unit_path},
                "recoveryEmail": {recovery_email},
                "recoveryPhone": {recovery_phone}
            }}"""
        },
        "sign_out": {
            "method": "POST",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}/signOut",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user.security"
                ]
            }
        },
        "undelete": {
            "method": "POST",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}/undelete",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user"
                ]
            },
            "payload": """{{
                "orgUnitPath": {org_unit_path}
            }}"""
        },
        "update": {
            "method": "PUT",
            "url": "https://www.googleapis.com/admin/directory/v1/users/{user_key}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user"
                ]
            },
            "payload": """{{
                "id": {id},
                "primaryEmail": {primary_email},
                "password": {password},
                "hashFunction": {hash_function},
                "suspended": {suspended},
                "changePasswordAtNextLogin": {change_password_at_next_login},
                "ipWhitelisted": {ip_whitelisted},
                "name": {{
                    "familyName": {family_name},
                    "givenName": {given_name}
                }},
                "emails": {emails},
                "externalIds": {external_ids},
                "relations": {relations},
                "addresses": {addresses},
                "organizations": {organizations},
                "phones": {phones},
                "languages": {languages},
                "posixAccounts": {posix_accounts},
                "sshPublicKeys": {ssh_public_keys},
                "notes": {notes},
                "websites": {websites},
                "locations": {locations},
                "includeInGlobalAddressList": {include_in_global_address_list},
                "keywords": {keywords},
                "gender": {gender},
                "ims": {ims},
                "customSchemas": {custom_schemas},
                "archived": {archived},
                "orgUnitPath": {org_unit_path},
                "recoveryEmail": {recovery_email},
                "recoveryPhone": {recovery_phone}
            }}"""
        },
        "watch": {
            "method": "POST",
            "url": "https://www.googleapis.com/admin/directory/v1/users/watch",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user.readonly",
                    "https://www.googleapis.com/auth/admin.directory.user",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "domain": {domain},
                "customer": {customer},
                "event": {event},
                "customFieldMask": {custom_field_mask},
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
    "Tokens": {
        "list": {
            "method": "GET",
            "url": "https://admin.googleapis.com/admin/directory/v1/users/{user_key}/tokens",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/admin.directory.user.security"
                ]
            }
        }
    }
}
