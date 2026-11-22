from fastapi.testclient import TestClient

from app.main import app

import pytest

client = TestClient(app)

@pytest.mark.integration
class TestFareAPI:
    def test_fare_api(self):
        fare_input = {
            "distance":5,
            "duration":15,
            "datetime_str": "2026-11-16T08:51:00",
            "demand": 20,
            "supply": 3,
            "is_airport":False, 
            "partner_cc": False,
            "promo_name": None
        }

        response = client.post(
            "/calculate-fare",
            json=fare_input
        )

        result = response.json()

        print(response.status_code)
        print(result)

        assert response.status_code == 201
        assert result["total_fare"] >= 0