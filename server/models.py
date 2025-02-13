from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    # Relationship with reviews (Task #1)
    reviews = db.relationship('Review', back_populates='customer')
    
    # Association proxy to get items reviewed by the customer (Task #2)
    items = association_proxy('reviews', 'item')
    
    # Serialization rules (Task #3)
    serialize_rules = ('-reviews.customer',)

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    # Relationship with reviews (Task #1)
    reviews = db.relationship('Review', back_populates='item')
    
    # Serialization rules (Task #3)
    serialize_rules = ('-reviews.item',)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    
    # Foreign keys (Task #1)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    
    # Relationships (Task #1)
    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')
    
    # Serialization rules (Task #3)
    serialize_rules = ('-customer.reviews', '-item.reviews',)
