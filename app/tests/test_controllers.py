# import pytest
# import json
#
# from app import app, db
#
#
# @pytest.fixture()
# def app():
#     app = app
#     app.config.update({
#         "TESTING": True,
#     })
#
#     # other setup can go here
#
#     yield app
#
#     # clean up / reset resources here
#
#
# @pytest.fixture()
# def client(app):
#     return app.test_client()
#
#
# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()
#
#
# def test_successful_creation(client):
#     # Given
#     payload = {
#         "name": "Serena Wu Luoyu",
#         "dob": "2000-07-15",
#     }
#
#     # When
#     response = client.post('/customer/create', json=payload)
#
#     # Then
#     # self.assertEqual(str, type(response.json['customer_id']))
#     # self.assertEqual(200, response.status_code)
#     print('the response is')
#     print(response)
#
# # def tearDown(self):
# #     for collection in self.db.list_collection_names():
# #         self.db.drop_collection(collection)
