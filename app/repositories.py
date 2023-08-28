from app.models import User
from app import db
import json
import os


class UserRepository:
    def create_user(self,json_filename):
        app_directory = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(app_directory, json_filename)
        with open(json_path, 'r') as json_file:
            user_data_list = json.load(json_file)

        for user_data in user_data_list:
            existing_user = self.check_user_by_id(user_data['id'])
            if existing_user:
                continue
            else:
                user = User(**user_data)
                db.session.add(user)
                db.session.commit()

    def check_user_by_id(self,id):
        return User.query.filter_by(id=id).first()


    def check_user_by_field(self, field, value):
        return User.query.filter_by(**{field: value}).first()


























