Maps = {
    "DataSets": {
        "get": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            }
        },
        "list": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "maxResults": {max_results},
                "pageToken": {page_token},
                "all": {all},
                "filter": {filter}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "datasetReference": {{
                    "datasetId": {reference_dataset_id},
                    "projectId": {reference_project_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "defaultTableExpirationMs": {default_table_expiration_ms},
                "defaultPartitionExpirationMs": {default_partition_expiration_ms},
                "labels": {labels},
                "access": {access},
                "creationTime": {creation_time},
                "lastModifiedTime": {last_modified_time},
                "location": {location},
                "defaultEncryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }},
                "satisfiesPzs": {satisfies_pzs}
            }}"""
        },
        "delete": {
            "method": "DELETE",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "deleteContents": {delete_contents}
            }}"""
        },
        "patch": {
            "method": "PATCH",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "datasetReference": {{
                    "datasetId": {reference_dataset_id},
                    "projectId": {reference_project_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "defaultTableExpirationMs": {default_table_expiration_ms},
                "defaultPartitionExpirationMs": {default_partition_expiration_ms},
                "labels": {labels},
                "access": {access},
                "creationTime": {creation_time},
                "lastModifiedTime": {last_modified_time},
                "location": {location},
                "defaultEncryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }},
                "satisfiesPzs": {satisfies_pzs}
            }}"""
        },
        "update": {
            "method": "PUT",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "datasetReference": {{
                    "datasetId": {reference_dataset_id},
                    "projectId": {reference_project_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "defaultTableExpirationMs": {default_table_expiration_ms},
                "defaultPartitionExpirationMs": {default_partition_expiration_ms},
                "labels": {labels},
                "access": {access},
                "creationTime": {creation_time},
                "lastModifiedTime": {last_modified_time},
                "location": {location},
                "defaultEncryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }},
                "satisfiesPzs": {satisfies_pzs}
            }}"""
        }
    },
    "Jobs": {
        "cancel": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/jobs/{job_id}/cancel",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "location": {location}
            }}"""
        },
        "get": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/jobs/{job_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "location": {location}
            }}"""
        },
        "get_query_results": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/queries/{job_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "startIndex": {start_index},
                "pageToken": {page_token},
                "maxResults": {max_results},
                "timeoutMs": {timeout_ms},
                "location": {location},
                "formatOptions": {{
                    "useInt64Timestamp": {use_int64_timestamp}
                }}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/upload/bigquery/v2/projects/{project_id}/jobs",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/devstorage.full_control",
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/devstorage.read_write"
                ]
            },
            "payload": """{{
                "configuration": {configuration},
                "jobReference": {jobReference}
            }}"""
        },
        "insert_metadata": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/jobs",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/devstorage.full_control",
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/devstorage.read_write"
                ]
            },
            "payload": """{{
                "configuration": {configuration},
                "jobReference": {jobReference}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/jobs",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "allUsers": {all_users},
                "maxResults": {max_results},
                "minCreationTime": {min_creation_time},
                "maxCreationTime": {max_creation_time},
                "pageToken": {page_token},
                "projection": {projection},
                "stateFilter": {state_filter},
                "parentJobId": {parent_job_id}
            }}"""
        },
        "query": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/queries",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "payload": """{{
                "kind": {kind},
                "query": {query},
                "maxResults": {max_results},
                "defaultDataset": {{
                    "datasetId": {default_dataset_id},
                    "projectId": {default_project_id}
                }},
                "timeoutMs": {timeout_ms},
                "dryRun": {dry_run},
                "useQueryCache": {use_query_cache},
                "useLegacySql": {use_legacy_sql},
                "parameterMode": {parameter_mode},
                "queryParameters": {query_parameters},
                "location": {location},
                "formatOptions": {{
                    "useInt64Timestamp": {use_int64_timestamp}
                }},
                "connectionProperties": {connection_properties},
                "labels": {labels},
                "maximumBytesBilled": {maximum_bytes_billed},
                "requestId": {request_id}
            }}"""
        }
    },
    "Projects": {
        "service_account": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/serviceAccount",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            }
        },
        "list": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "maxResults": {max_results},
                "pageToken": {page_token}
            }}"""
        }
    },
    "TableData": {
        "insert_all": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}/insertAll",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.insertdata"
                ]
            },
            "payload": """{{
                "kind": {kind},
                "skipInvalidRows": {skip_invalid_rows},
                "ignoreUnknownValues": {ignore_unknown_values},
                "templateSuffix": {template_suffix},
                "rows": {rows},
                "traceId": {trace_id}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}/data",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "startIndex": {start_index},
                "maxResults": {max_results},
                "pageToken": {page_token},
                "selectedFields": {selected_fields},
                "formatOptions": {{
                    "useInt64Timestamp": {use_int64_timestamp}
                }}
            }}"""
        }
    },
    "Tables": {
        "delete": {
            "method": "DELETE",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            }
        },
        "get": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "selectedFields": {selected_fields}
            }}"""
        },
        "get_iam_policy": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}:getIamPolicy",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "payload": """{{
                "requestedPolicyVersion": {requested_policy_version}
            }}"""
        },
        "insert": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "tableReference": {{
                    "projectId": {reference_project_id},
                    "datasetId": {reference_dataset_id},
                    "tableId": {reference_table_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "labels": {labels},
                "schema": {{
                    "fields": {schema_fields}
                }},
                "timePartitioning": {{
                    "type": {time_partitioning_type},
                    "expirationMs": {time_partitioning_expiration_ms},
                    "field": {time_partitioning_field},
                    "requirePartitionFilter": {time_partitioning_require_partition_filter}
                }},
                "rangePartitioning": {{
                    "field": {range_partitioning_field},
                    "range": {{
                        "start": {range_partitioning_start},
                        "end": {range_partitioning_end},
                        "interval": {range_partitioning_interval}
                    }}
                }},
                "clustering": {{
                    "fields": {clustering_fields}
                }},
                "requirePartitionFilter": {require_partition_filter},
                "expirationTime": {expiration_time},
                "externalDataConfiguration": {external_data_configuration},
                "encryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }}
            }}"""
        },
        "list": {
            "method": "GET",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "query": """{{
                "maxResults": {max_results},
                "pageToken": {page_token}
            }}"""
        },
        "patch": {
            "method": "PATCH",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "tableReference": {{
                    "projectId": {reference_project_id},
                    "datasetId": {reference_dataset_id},
                    "tableId": {reference_table_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "labels": {labels},
                "schema": {{
                    "fields": {schema_fields}
                }},
                "timePartitioning": {{
                    "type": {time_partitioning_type},
                    "expirationMs": {time_partitioning_expiration_ms},
                    "field": {time_partitioning_field},
                    "requirePartitionFilter": {time_partitioning_require_partition_filter}
                }},
                "rangePartitioning": {{
                    "field": {range_partitioning_field},
                    "range": {{
                        "start": {range_partitioning_start},
                        "end": {range_partitioning_end},
                        "interval": {range_partitioning_interval}
                    }}
                }},
                "clustering": {{
                    "fields": {clustering_fields}
                }},
                "requirePartitionFilter": {require_partition_filter},
                "expirationTime": {expiration_time},
                "externalDataConfiguration": {external_data_configuration},
                "encryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }}
            }}"""
        },
        "set_iam_policy": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}:setIamPolicy",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "policy": {policy},
                "updateMask": {update_mask}
            }}"""
        },
        "test_iam_policy": {
            "method": "POST",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}:testIamPolicy",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform",
                    "https://www.googleapis.com/auth/bigquery.readonly",
                    "https://www.googleapis.com/auth/cloud-platform.read-only"
                ]
            },
            "payload": """{{
                "permissions": {permissions}
            }}"""
        },
        "update": {
            "method": "PUT",
            "url": "https://bigquery.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/bigquery",
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "tableReference": {{
                    "projectId": {reference_project_id},
                    "datasetId": {reference_dataset_id},
                    "tableId": {reference_table_id}
                }},
                "friendlyName": {friendly_name},
                "description": {description},
                "labels": {labels},
                "schema": {{
                    "fields": {schema_fields}
                }},
                "timePartitioning": {{
                    "type": {time_partitioning_type},
                    "expirationMs": {time_partitioning_expiration_ms},
                    "field": {time_partitioning_field},
                    "requirePartitionFilter": {time_partitioning_require_partition_filter}
                }},
                "rangePartitioning": {{
                    "field": {range_partitioning_field},
                    "range": {{
                        "start": {range_partitioning_start},
                        "end": {range_partitioning_end},
                        "interval": {range_partitioning_interval}
                    }}
                }},
                "clustering": {{
                    "fields": {clustering_fields}
                }},
                "requirePartitionFilter": {require_partition_filter},
                "expirationTime": {expiration_time},
                "externalDataConfiguration": {external_data_configuration},
                "encryptionConfiguration": {{
                    "kmsKeyName": {kms_key_name}
                }}
            }}"""
        }
    }
}
