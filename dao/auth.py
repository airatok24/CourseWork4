from dao.model.user import User
from flask import abort


class AuthUserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, item_id):
        item = self.session.query(User).filter(User.id == item_id).one_or_none()
        return item

    def get_one_by_email(self, item_data):
        email = item_data.get("email")
        item = self.session.query(User).filter(User.email == email).one_or_none()
        return item

    def get_all(self):
        items = self.session.query(User).all()
        return items

    def create(self, item_data):
        new_data = User(**item_data)
        self.session.add(new_data)
        self.session.commit()
        return new_data

    def update(self, new_data):
        item_id = new_data.get("id")
        if item_id is None:
            abort(401)

        item = self.session.query(User).filter(User.id == item_id).update(new_data)
        self.session.commit()

    def delete(self, item_id):
        item = self.get_one(item_id)
        self.session.delete(item)
        self.session.commit()