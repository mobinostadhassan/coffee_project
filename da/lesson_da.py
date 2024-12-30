from da.tools.database_manager import *
from model.lesson import Lesson

session = get_session()


def save(order):
    session.add(order)
    session.commit()


def edit(order):
    session.merge(order)
    session.commit()


def remove(order):
    session.delete(order)
    session.commit()


def find_all():
    return session.query(order).all()


def find_by_id(order_id):
    return session.query(order).get(order_id)


