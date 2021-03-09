# from functools import wraps
# from bson import ObjectId
# from datetime import datetime, date, timedelta
# from flask import Flask, request, jsonify, abort
# import json
# from app.main.service.auth_helper import Auth
# from http import HTTPStatus
# from app.main.util.CustomMessage import CustomSuccess, CustomError, ResponseStatus
# from app.main.service.response_service import ResponseService
#
#
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         data, status = Auth.get_logged_in_user(request)
#         token = data.get('data')
#         if not token:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.INVALID_TOKEN.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#         request.user = token
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# def admin_token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         data, status = Auth.get_logged_in_admin(request)
#         token = data.get('data')
#
#         if not token:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.INVALID_TOKEN.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#         request.admin = token
#         admin = token.get('admin')
#         if not admin:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.ADMIN_TOKEN_REQUIRED.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# def super_admin_token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         data, status = Auth.get_logged_in_admin(request)
#         token = data.get('data')
#
#         if not token:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.INVALID_TOKEN.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#         request.admin = token
#         admin = token.get('admin')
#         if admin != 'SuperAdmin':
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.SUPER_ADMIN_TOKEN_REQUIRED.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# def pharmacyAdmin_token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         data, status = Auth.get_logged_in_admin(request)
#         token = data.get('data')
#
#         if not token:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.INVALID_TOKEN.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#         request.admin = token
#         admin = token.get('admin')
#         if admin not in ['SuperAdmin', 'PharmacyAdmin']:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.ADMIN_TOKEN_REQUIRED.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# def storeAdmin_token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#
#         data, status = Auth.get_logged_in_admin(request)
#         token = data.get('data')
#
#         if not token:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.INVALID_TOKEN.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#         request.admin = token
#         admin = token.get('admin')
#         if admin not in ['SuperAdmin', 'StoreAdmin', 'PharmacyAdmin']:
#             return ResponseService.build(None, HTTPStatus.UNAUTHORIZED.value,
#                                          ResponseStatus.FAILURE.value,
#                                          CustomError.ADMIN_TOKEN_REQUIRED.value), HTTPStatus.UNAUTHORIZED.value, {
#                        'Content-Type': 'application/json'}
#
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, (ObjectId, datetime)):
#             return str(o)
#         return json.JSONEncoder.default(self, o)
#
#
# JSONEncode = JSONEncoder(indent=2)
