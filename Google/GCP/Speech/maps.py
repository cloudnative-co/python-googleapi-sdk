Maps = {
    "Speech": {
        "get": {
            "method": "GET",
            "url": "https://speech.googleapis.com/v1/operations/{name}",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            }
        },
        "list": {
            "method": "GET",
            "url": "https://speech.googleapis.com/v1/operations",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "query": """{{
                "name": {name},
                "filter": {filter},
                "pageSize": {page_size},
                "pageToken": {page_token}
            }}"""
        },
        "recognize": {
            "method": "POST",
            "url": "https://speech.googleapis.com/v1/speech:recognize",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "audio": {{
                    "uri": {uri},
                    "content": {content}
                }},
                "config": {{
                    "encoding": {encoding},
                    "sampleRateHertz": {sample_rate_hertz},
                    "audioChannelCount": {audio_channel_count},
                    "enableSeparateRecognitionPerChannel": {enable_separate_recognition_per_channel},
                    "languageCode":{language_code},
                    "maxAlternatives": {max_alternatives},
                    "profanityFilter": {profanity_filter},
                    "speechContexts": {speech_contexts},
                    "enableWordTimeOffsets": {enable_word_time_offsets},
                    "enableAutomaticPunctuation": {enable_automatic_punctuation},
                    "diarizationConfig": {{
                          "enableSpeakerDiarization": {enable_speaker_diarization},
                          "minSpeakerCount": {min_speaker_count},
                          "maxSpeakerCount": {max_speaker_count},
                          "speakerTag": {speaker_tag}
                    }},
                    "metadata": {{
                         "interactionType": {interaction_type},
                         "industryNaicsCodeOfAudio": {industry_naics_code_of_audio},
                         "microphoneDistance": {microphone_distance},
                         "originalMediaType" :{original_media_type},
                         "recordingDeviceType": {recording_device_type},
                         "recordingDeviceName": {recording_device_name},
                         "originalMimeType": {original_mime_type},
                         "audioTopic": {audio_topic}
                    }},
                    "model": {model},
                    "useEnhanced": {use_enhanced}
                }}
            }}"""
        },
        "longrunningrecognize": {
            "method": "POST",
            "url": "https://speech.googleapis.com/v1/speech:longrunningrecognize",
            "auth_method": "gsuite_autholization",
            "auth_params": {
                "scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ]
            },
            "payload": """{{
                "audio": {{
                    "uri": {uri},
                    "content": {content}
                }},
                "config": {{
                    "encoding": {encoding},
                    "sampleRateHertz": {sample_rate_hertz},
                    "audioChannelCount": {audio_channel_count},
                    "enableSeparateRecognitionPerChannel": {enable_separate_recognition_per_channel},
                    "languageCode":{language_code},
                    "maxAlternatives": {max_alternatives},
                    "profanityFilter": {profanity_filter},
                    "speechContexts": {speech_contexts},
                    "enableWordTimeOffsets": {enable_word_time_offsets},
                    "enableAutomaticPunctuation": {enable_automatic_punctuation},
                    "diarizationConfig": {{
                          "enableSpeakerDiarization": {enable_speaker_diarization},
                          "minSpeakerCount": {min_speaker_count},
                          "maxSpeakerCount": {max_speaker_count},
                          "speakerTag": {speaker_tag}
                    }},
                    "metadata": {{
                         "interactionType": {interaction_type},
                         "industryNaicsCodeOfAudio": {industry_naics_code_of_audio},
                         "microphoneDistance": {microphone_distance},
                         "originalMediaType" :{original_media_type},
                         "recordingDeviceType": {recording_device_type},
                         "recordingDeviceName": {recording_device_name},
                         "originalMimeType": {original_mime_type},
                         "audioTopic": {audio_topic}
                    }},
                    "model": {model},
                    "useEnhanced": {use_enhanced}
                }}
            }}"""
        }
    }
}
