from flask_restx import Resource, Namespace
from flask import request, abort
from container import user_service
from utils import generate_tokens, decode_token, auth_required

user_profile_ns = Namespace('user')


@user_profile_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        """
        показывает информацию из профиля пользователя
        """
        new_data = request.json
        return user_service.get_one_by_email(new_data), 200

    @auth_required
    def patch(self):
        """
        изменяет информацию пользователя (имя, фамилия, любимый жанр)
        """
        new_data = request.json
        user_db = user_service.get_one_by_email(new_data)
        print(f"user_db - {user_db}")

        user_role = new_data.get("role")
        if user_role != "user":
            abort(400)

        user_service.update_by_email(new_data)
        return "", 204


@user_profile_ns.route('/password')
class UsersView(Resource):
    @auth_required
    def put(self):
        """
        обновляет пароль пользователя
        """
        new_data = request.json
        # получаем 2 хэша старого и нового паролей пользователя
        user_service.hash_old_new_passwords(new_data)
        print(f"new_data with passwords - {new_data}")

        user_db = user_service.get_one_by_email(new_data)
        print(f"user_db - {user_db}")
        password_db = user_db["password"]

        if new_data["password_old"] != password_db:
            return {"error": "Неверные учётные данные"}, 401

        new_hashed_password = new_data["password_new"]
        user_db["password"] = new_hashed_password

        data_to_update = {
            "email": user_db["email"],
            "password": user_db["password"]
        }

        user_service.update_by_email(data_to_update)

        # генерируем токены.
        data = {
            "email": user_db["email"],
            "role": user_db["role"]
        }

        print(data)
        return generate_tokens(data), 201