Maps = {
    "SpreadSheets": {
        "get": {
            "method": "GET",
            "url": "https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/drive",
                    "https://www.googleapis.com/auth/drive.readonly",
                    "https://www.googleapis.com/auth/drive.file",
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/spreadsheets.readonly"
                ]
            },
            "query": """{{
                "ranges": {ranges},
                "includeGridData": {include_grid_data}
            }}"""
        }
    },
    "Values": {
        "get": {
            "method": "GET",
            "url": "https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/drive",
                    "https://www.googleapis.com/auth/drive.readonly",
                    "https://www.googleapis.com/auth/drive.file",
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/spreadsheets.readonly"
                ]
            },
            "query": """{{
                "majorDimension": {major_dimension},
                "valueRenderOption": {value_render_option},
                "dateTimeRenderOption": {date_time_render_option}
            }}"""
        }
    }
}
