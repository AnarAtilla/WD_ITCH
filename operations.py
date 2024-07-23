from sqlalchemy.sql import func
from models import Category, Product
from database import Session

session = Session()

def add_categories_and_products():
    categories = [
        Category(name="Электроника", description="Гаджеты и устройства."),
        Category(name="Книги", description="Печатные книги и электронные книги."),
        Category(name="Одежда", description="Одежда для мужчин и женщин.")
    ]
    session.add_all(categories)
    session.commit()

    products = [
        Product(name="Смартфон", price=299.99, in_stock=True, category=categories[0]),
        Product(name="Ноутбук", price=499.99, in_stock=True, category=categories[0]),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=categories[1]),
        Product(name="Джинсы", price=40.50, in_stock=True, category=categories[2]),
        Product(name="Футболка", price=20.00, in_stock=True, category=categories[2])
    ]
    session.add_all(products)
    session.commit()

def read_categories_and_products():
    categories = session.query(Category).all()
    for category in categories:
        print(f"Category: {category.name}")
        for product in category.products:
            print(f"  Product: {product.name}, Price: {product.price}")

def update_product_price():
    product = session.query(Product).filter_by(name="Смартфон").first()
    if product:
        product.price = 349.99
        session.commit()

def aggregate_and_group_products():
    result = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()
    for category_name, product_count in result:
        print(f"Category: {category_name}, Product Count: {product_count}")

def filter_categories_with_multiple_products():
    result = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()
    for category_name, product_count in result:
        print(f"Category: {category_name}, Product Count: {product_count}")

def close_session():
    session.close()