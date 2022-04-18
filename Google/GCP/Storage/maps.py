Maps = {
    "Buckets": {
        "delete": {
            "method": "DELETE",
            "url": "https://storage.googleapis.com/storage/v1/b/{bucket}/o/{name}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.full_control",
                    "https://www.googleapis.com/auth/devstorage.read_write",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "ifMetagenerationMatch": {if_metageneration_match},
                "ifMetagenerationNotMatch": {if_metageneration_not_match}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://storage.googleapis.com/storage/v1/b/{bucket}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "ifMetagenerationMatch": {if_metageneration_match},
                "ifMetagenerationNotMatch": {if_metageneration_not_match},
                "projection": {projection}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://storage.googleapis.com/storage/v1/b",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.full_control",
                    "https://www.googleapis.com/auth/devstorage.read_write",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "project": {project},
                "predefinedAcl": {predefined_acl},
                "predefinedDefaultObjectAcl": {predefined_default_object_acl},
                "projection": {projection}
            }}""",
            "payload": """{{
                "name": {name},
                "acl": {acl},
                "biling": {{
                    "requesterPays": {requester_pays}
                }},
                "cors": {cors},
                "defaultEventBasedHold": {default_event_based_hold},
                "defaultObjectAcl": {default_object_acl},
                "encryption": {{
                    "defaultKmsKeyName": {default_kms_key_name}
                }},
                "iamConfiguration": {{
                    "uniformBucketLevelAccess": {{
                        "enabled": {uniform_bucket_level_access}
                    }}
                }},
                "labels": {labels},
                "lifecycle": {lifecycle},
                "location": {location},
                "logging": {{
                    "logBucket": {log_bucket},
                    "logObjectPrefix": {log_object_prefix}
                }},
                "retentionPolicy": {{
                    "retentionPeriod": {retention_period}
                }},
                "storageClass": {storage_class},
                "versioning": {{
                    "enabled": {versioning}
                }},
                "website": {{
                    "mainPageSuffix": {main_page_suffix},
                    "notFoundPage": {not_found_page}
                }}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://storage.googleapis.com/storage/v1/b",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "project": {project},
                "maxResult": {max_result},
                "pageToken": {page_token},
                "prefix": {prefix},
                "projection": {projection}
            }}"""
        }
    },
    "Objects": {
        "delete": {
            "method": "DELETE",
            "url": "https://storage.googleapis.com/storage/v1/b/{bucket}/o/{name}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.full_control",
                    "https://www.googleapis.com/auth/devstorage.read_write",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "generation": {generation},
                "ifGenerationMatch": {if_generation_match},
                "ifGenerationNotMatch": {if_generation_not_match},
                "ifMetagenerationMatch": {if_metageneration_match},
                "ifMetagenerationNotMatch": {if_metageneration_not_match}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://storage.googleapis.com/storage/v1/b/{bucket}/o/{name}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "alt": {alt},
                "generation": {generation},
                "ifGenerationMatch": {if_generation_match},
                "ifGenerationNotMatch": {if_generation_not_match},
                "ifMetagenerationMatch": {if_metageneration_match},
                "ifMetagenerationNotMatch": {if_metageneration_not_match},
                "projection": {projection}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://storage.googleapis.com/upload/storage/v1/b/{bucket}/o",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "name":{name},
                "uploadType":{upload_type},
                "contentEncoding":{content_encoding},
                "ifGenerationMatch":{if_generation_match},
                "ifGenerationNotMatch":{if_generation_not_match},
                "ifMetagenerationMatch":{if_metageneration_match},
                "ifMetagenerationNotMatch":{if_metageneration_not_match},
                "kmsKeyName":{kms_key_name},
                "predefinedAcl":{predefined_acl},
                "projection":{projection}
            }}""",
            "payload": """{{
                "acl": {acl},
                "cacheControl": {cache_control},
                "contentDisposition": {content_disposition},
                "contentEncoding": {content_encoding},
                "contentLanguage": {content_language},
                "contentType": {content_type},
                "crc32c": {crc32c},
                "customTime": {custom_time},
                "eventBasedHold": {event_based_hold},
                "md5Hash": {md5_hash},
                "metadata": {metadata},
                "name": {name},
                "storageClass": {storage_class},
                "temporaryHold": {temporary_hold}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://storage.googleapis.com/storage/v1/b",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "delimiter": {delimiter},
                "endOffset": {end_offset},
                "includeTrailingDelimiter": {include_trailing_delimiter},
                "maxResult": {max_result},
                "pageToken": {page_token},
                "prefix": {prefix},
                "projection": {projection},
                "startOffset": {start_offset},
                "versions": {versions}
            }}"""
        }
    }
}
