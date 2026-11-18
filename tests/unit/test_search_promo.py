import pytest

from app.services import search_promo

from app.schemas.rule_engine_schema import PromoRule

class TestSearchPromo:
    @pytest.mark.parametrize(
            "promo_name, expected",
            [
                ("FLYAWAY", PromoRule),
                ("WALLETSAVE", PromoRule),
                ("LOVEDELIVERED", None), #existing promo is_active is set False
                ("NON EXISTENT PROMO", None) #promo does not exist
            ]
    )
    def test_search_promo(self, promo_name, expected):
        result = search_promo.find_promo(promo_name=promo_name)
        
        if result is None:
            assert result is None
        else:
            assert isinstance(result, expected)
