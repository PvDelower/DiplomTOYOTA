# services/users/src/api/__init__.py


from flask_restx import Api


from src.api.cars.views import cars_namespace

api = Api(version="1.0", title="Cars API", doc="/doc")

api.add_namespace(cars_namespace, path="/users")
