import io

from ...base import Base
from ...utilities import request_parameter


class Speech(Base):

    def get(self, name: str):
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self, name: str = None, filter: str = None,
        page_size: int = None, page_token: str = None
    ):
        request = request_parameter(locals())
        return self.http_request(**request)

    def recognize(
        self,
        uri: str = None, content: bytes = None,
        encoding: str = None, sample_rate_hertz: int = None,
        audio_channel_count: int = None,
        enable_separate_recognition_per_channel: bool = None,
        language_code: str = None, max_alternatives: int = None,
        profanity_filter: bool = None, speech_contexts: list = None,
        enable_word_time_offsets: bool = None, enable_automatic_punctuation: bool = None,
        enable_speaker_diarization: bool = None, min_speaker_count: int = None,
        max_speaker_count: int = None, speaker_tag: int = None,
        interaction_type: str = None, industry_naics_code_of_audio: int = None,
        microphone_distance: str = None, original_media_type: str = None,
        recording_device_type: str = None, recording_device_name: str = None,
        original_mime_type: str = None, audio_topic: str = None,
        model: str = None, use_enhanced: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def longrunningrecognize(
        self,
        uri: str = None, content: bytes = None,
        encoding: str = None, sample_rate_hertz: int = None,
        audio_channel_count: int = None,
        enable_separate_recognition_per_channel: bool = None,
        language_code: str = None, max_alternatives: int = None,
        profanity_filter: bool = None, speech_contexts: list = None,
        enable_word_time_offsets: bool = None, enable_automatic_punctuation: bool = None,
        enable_speaker_diarization: bool = None, min_speaker_count: int = None,
        max_speaker_count: int = None, speaker_tag: int = None,
        interaction_type: str = None, industry_naics_code_of_audio: int = None,
        microphone_distance: str = None, original_media_type: str = None,
        recording_device_type: str = None, recording_device_name: str = None,
        original_mime_type: str = None, audio_topic: str = None,
        model: str = None, use_enhanced: bool = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
