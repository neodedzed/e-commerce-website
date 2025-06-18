from database.models.product_model import Product


def read_all_products(db):
    return db.query(Product).all()