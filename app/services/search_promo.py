from app.rules import promos

from app.schemas.rule_engine_schema import PromoRule

def find_promo(promo_name: str, 
                 promo_rules: list[PromoRule] = promos.PROMO_RULES) -> PromoRule | None:
    """
    Searches a promo based on its name. An iterator is being used to find the first match.

    Args:
        promo_name: the name of the promo that is being searched
        promo_rules: a list of promos that have been created all time
    Returns:
        PromoRule | None: The singular PromoRule. If no Promo is foud then None will be returned
    """
    promo = next(
        (promo for promo in promo_rules if (promo.name == promo_name) and (promo.active == True)), 
        None
        )

    return promo