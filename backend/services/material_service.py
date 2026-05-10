from models.prediction import Prediction
from extensions import db
from ml.material_predictor import predict_best_material

def recommend_material(input_data):
    # Call ML (rule-based for now)
    prediction = predict_best_material(input_data)

    # Save prediction to DB
    record = Prediction(
        product_category=input_data.get("product_category"),
        product_weight=input_data.get("product_weight"),
        fragility_level=input_data.get("fragility_level"),
        is_liquid=input_data.get("is_liquid"),
        recommended_material=prediction["recommended_material"],
        suitability_score=prediction["suitability_score"]
    )

    db.session.add(record)
    db.session.commit()

    return prediction
