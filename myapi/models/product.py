import datetime as dt

from myapi.database import db, Model, SurrogatePK
from myapi.extensions import ma


class Product(Model):
    """Model for a product record"""

    __tablename__ = 'products'
    product_id = db.Column(db.Integer, unique=True, nullable=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, product_id=product_id, name=name,
                 value=value, **kwargs):
        """Create instance."""
        db.Model.__init__(self, product_id=product_id, name=name,
                          value=value, **kwargs)

    def __repr__(self):
        return (
            '<Product('
            '{product_id},'
            '{name},'
            '{value},'
            '{created_at})>'.format(
                product_id=self.product_id,
                name=self.name,
                value=self.value,
                created_at=self.created_at
            )
        )


class ProductSchema(ma.ModelSchema):

    class Meta:
        model = Product
        sqla_session = db.session

