import pytest

from datetime import datetime

from app.services import create_hash

class TestHashFunc:
    def test_hash_format_length(self):
        fare_input = {
            "fare":250,
            "datetime_str":"some_datetime"
        }
        
        result = create_hash.create_hash(fare_input=fare_input)

        assert isinstance(result, str)
        assert len(result) == 64

    def test_same_key_different_order(self):
        fare_input_1 = {
            "fare": 250,
            "datetime_str": "some_datetime"
        }
        result_1 = create_hash.create_hash(fare_input_1)


        fare_input_2 = {
            "datetime_str": "some_datetime",
            "fare": 250,
        }
        result_2 = create_hash.create_hash(fare_input_2)
        
        #compare results
        assert result_1 == result_2

    def test_different_dtyes(self):
        fare_input = {
            "fare":150,
            "is_cc_supported":True,
            "date_requested":datetime(2026, 10, 2)
        }

        result = create_hash.create_hash(fare_input=fare_input)

        assert len(result) == 64