from sqlalchemy import create_engine, ForeignKey, Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, sessionmaker, relationship

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'Supplier'
    SupplierId = Column(Integer,primary_key=True)
    Name = Column(String)

class Product(Base):
    __tablename__ = 'Products'
    ProductId = Column(Integer, primary_key=True)
    Name = Column(String)
    SupplierId = Column(Integer,ForeignKey('Supplier.SupplierId'))
    supplier = relationship(
        Supplier,
        backref=backref('Supplier',uselist = True, cascade = 'delete,all')
    )

db = create_engine('sqlite:///database.db', echo = True)
Base.metadata.bind = db
Base.metadata.create_all()

Session = sessionmaker(bind = db)
ses = Session()
#supplier = Supplier(Name = 'Vendor 1')
#supplier2 = Supplier(Name = 'Vendor 2')
#ses.add(supplier)
#ses.add(supplier2)
#ses.add_all(
#    [
#        Product(Name = 'Soap', SupplierId=supplier.SupplierId),
#        Product(Name = 'Gasoline', SupplierId=supplier.SupplierId),
#        Product(Name = 'Wood Stock', SupplierId=supplier.SupplierId),
#    ]
#)
#ses.commit()

results = ses.query(Product).all()
for prod in results:
    print(prod.Name)