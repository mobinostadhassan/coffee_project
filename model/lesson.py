from sqlalchemy import Integer, String, Column, Boolean

from base import Base


class order(Base):
    __tablename__ = 'order'
    _id = Column("id", Integer, primary_key=True)
    _name = Column("name", String(30))
    _order = Column("order", String(50))
    _quantity= Column("quantity", Integer)
    _price = Column("price", Integer)

    def __init__(self, id, name,order,quantity, price):
        self.id = id
        self.name = name
        self.order = order
        self.quantity =quantity
        self._price =price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def order(self):
        return self._order

    @order.setter
    def sefareshat(self, value):
        self._sefareshat = value

    @property
    def tedad(self):
        return self._tedad

    @tedad.setter
    def tedad(self, value):
        self._tedad = value


    @property
    def gheymat(self):
        return self._gheymat

    @gheymat.setter
    def gheymat(self, value):
        self._gheymat= value
