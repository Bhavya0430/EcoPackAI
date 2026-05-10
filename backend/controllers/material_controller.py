from flask import request, jsonify
from flask_jwt_extended import jwt_required
from services.material_service import recommend_material

@jwt_required()
def predict_material():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Input data required"}), 400

    result = recommend_material(data)

    return jsonify({
        "recommended_material": result["recommended_material"],
        "suitability_score": result["suitability_score"]
    }), 200
