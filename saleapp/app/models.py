from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
import hashlib
from enum import Enum as RoleEnum
from flask_login import UserMixin


class UserRole(RoleEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), nullable=True)
    # active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name



if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        u = User(name="admin", username="admin", password=str(hashlib.md5("123456".encode('utf-8')).hexdigest()),
                 avatar="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg",
                 user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        #
        # products = [{
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Galaxy Tab S9",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1679134375/ckvdo90ltnfns77zf1xb.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Galaxy Tab S9",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1679134375/ckvdo90ltnfns77zf1xb.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 2
        # }, {
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690011099/uobyqhus0bhqt1qbh1qp.jpg",
        #     "category_id": 1
        # }, {
        #     "name": "Galaxy Tab S9",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1679134375/ckvdo90ltnfns77zf1xb.jpg",
        #     "category_id": 2
        # }]
        #
        # for p in products:
        #     p = Product(**p)
        #     db.session.add(p)
        #
        # db.session.commit()