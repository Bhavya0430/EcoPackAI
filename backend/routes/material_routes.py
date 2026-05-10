from flask import Blueprint
from controllers.material_controller import predict_material

material_bp = Blueprint("material_bp", __name__)

material_bp.route("/predict", methods=["POST"])(predict_material)
