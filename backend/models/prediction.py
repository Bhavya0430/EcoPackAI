from extensions import db

class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)

    product_category = db.Column(db.String(100))
    product_weight = db.Column(db.Float)
    fragility_level = db.Column(db.String(50))
    is_liquid = db.Column(db.Boolean)

    recommended_material = db.Column(db.String(100))
    suitability_score = db.Column(db.Float)

    def __repr__(self):
        return f"<Prediction {self.recommended_material}>"
