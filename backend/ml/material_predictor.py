def predict_best_material(input_data):
    """
    Simulated ML logic for material recommendation.
    """

    product_weight = input_data.get("product_weight", 0)
    fragility = input_data.get("fragility_level", "").lower()
    is_liquid = input_data.get("is_liquid", False)

    if is_liquid and fragility == "high":
        return {
            "recommended_material": "Glass",
            "suitability_score": 0.85
        }

    if product_weight > 2:
        return {
            "recommended_material": "Corrugated Box",
            "suitability_score": 0.78
        }

    return {
        "recommended_material": "Bioplastic",
        "suitability_score": 0.82
    }
