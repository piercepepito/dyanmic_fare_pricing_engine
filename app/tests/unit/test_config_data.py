import pytest

from app import config

class TestConfigValidation:
    @pytest.mark.parametrize(
            "key, value, error_response",
            [
             ("BASE_FARE", -5, "Base fare should be greater than 0"),
             ("DURATION_RATE", -2, "Duration rate should be greater than 0"),
             ("DISTANCE_RATE", 0, "Distance rate should be greater than 0")
            ]
    )
    def test_invalid_config(self, key, value, error_response, monkeypatch):
        monkeypatch.setattr(config, key, value)

        with pytest.raises(ValueError) as e:
            config.config_data_validation()

        assert error_response == str(e.value)
    