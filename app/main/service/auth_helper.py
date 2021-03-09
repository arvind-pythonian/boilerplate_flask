# import json
# import sys
#
#
# class Auth:
#
#     @staticmethod
#     def login_user(data):
#         try:
#             email = data.get('email')
#             password = data.get('password')
#             # UserService.create_user(data)
#             # fetch the user data
#             user = User.objects.get({'email': email})
#             if user and User.check_password(password, user.password):
#                 auth_token = User.encode_auth_token(user._id)
#                 if auth_token:
#                     response_object = {
#                         'status': 'success',
#                         'token': auth_token.decode(),
#                         'code': 200
#                     }
#                     return response_object
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'email or password does not match.',
#                     'code': 401
#                 }
#                 return response_object
#
#         except User.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Username or Password is incorrect',
#                 'code': 401
#             }
#             return response_object
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError as e:
#             print(e)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def login_admin(data):
#         try:
#             email = data.get('email')
#             password = data.get('password')
#             # UserService.create_user(data)
#             # fetch the user data
#             admin = Admin.objects.get({'email': email})
#             if admin and Admin.check_password(password, admin.password):
#                 auth_token = User.encode_auth_token(admin._id)
#                 if auth_token:
#                     response_object = {
#                         'status': 'success',
#                         'code': 200,
#                         'data': {
#                             '_id': str(admin._id),
#                             'token': auth_token.decode(),
#                             'firstName': admin.firstName,
#                             'lastName': admin.lastName,
#                             'userName': admin.userName,
#                             'email': admin.email,
#                             'hospital': str(admin.hospital),
#                             'role': {
#                                 '_id': str(admin.role._id),
#                                 'roleName': admin.role.roleName
#                             },
#                             'isSuperAdmin': admin.isSuperAdmin,
#                             'IsFirstLogin': admin.IsFirstLogin
#                         }
#
#                     }
#                     return response_object
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'email or password does not match.',
#                     'code': 401
#                 }
#                 return response_object
#
#         except User.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Username or Password is incorrect',
#                 'code': 401
#             }
#             return response_object
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError:
#             print(ValueError)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def login_storeAdmin(data):
#         try:
#             email = data.get('email')
#             password = data.get('password')
#             # UserService.create_user(data)
#             # fetch the user data
#             sAdmin = storeAdmin.objects.get({'email': email})
#             if sAdmin and storeAdmin.check_password(password, sAdmin.password):
#                 auth_token = storeAdmin.encode_auth_token(sAdmin._id)
#                 if auth_token:
#                     response_object = {
#                         'status': 'success',
#                         'code': 200,
#                         'data': {
#                             '_id': str(sAdmin._id),
#                             'token': auth_token.decode(),
#                             'firstName': sAdmin.firstName,
#                             'lastName': sAdmin.lastName,
#                             'userName': sAdmin.userName,
#                             'email': sAdmin.email,
#                             'store': str(sAdmin.pharmacyId),
#                             'role': {
#                                 '_id': str(sAdmin.role._id),
#                                 'roleName': sAdmin.role.roleName
#                             },
#                             'isSuperAdmin': sAdmin.isSuperAdmin,
#                             'IsFirstLogin': sAdmin.IsFirstLogin
#                         }
#
#                     }
#                     return response_object
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'email or password does not match.',
#                     'code': 401
#                 }
#                 return response_object
#
#         except storeAdmin.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Username or Password is incorrect',
#                 'code': 401
#             }
#             return response_object
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError:
#             print(ValueError)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def logout_user(data):
#         if data:
#             auth_token = data.split(" ")[1]
#         else:
#             auth_token = ''
#         if auth_token:
#             resp = User.decode_auth_token(auth_token)
#             print(resp)
#         else:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Provide a valid auth token.'
#             }
#             return response_object, 403
#
#     @staticmethod
#     def get_logged_in_admin(new_request):
#         try:
#             # get the auth token
#             auth_token = new_request.headers.get('Authorization')
#             if auth_token:
#                 resp = User.decode_auth_token(auth_token)
#                 if not isinstance(resp, str):
#                     adminId = ObjectId(resp['sub'])
#                     admin = Admin.objects.get({'_id': adminId})
#                     response_object = {
#                         'status': 'success',
#                         'data': {
#                             'adminId': admin._id,
#                             'email': admin.email,
#                             'admin': admin.role.roleName,
#                             'pharmacyId': admin.pharmacy
#                             # 'registered_on': str(user.registered_on)
#                         }
#                     }
#                     return response_object, 200
#
#                 response_object = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return response_object, 401
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'Invalid auth token.'
#                 }
#                 return response_object, 401
#
#         except Admin.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Invalid auth token!',
#                 'code': 401
#             }
#             return response_object, 401
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError as e:
#             print(e)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def get_logged_in_user(new_request):
#         try:
#             # get the auth token
#             auth_token = new_request.headers.get('Authorization')
#             if auth_token:
#                 resp = User.decode_auth_token(auth_token)
#                 if not isinstance(resp, str):
#                     userId = ObjectId(resp['sub'])
#                     user = User.objects.get({'_id': userId})
#                     response_object = {
#                         'status': 'success',
#                         'data': {
#                             'user_id': user._id,
#                             'email': user.email,
#                             # 'admin': user.admin,
#                             # 'registered_on': str(user.registered_on)
#                         }
#                     }
#                     return response_object, 200
#
#                 response_object = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return response_object, 401
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'Invalid auth token.'
#                 }
#                 return response_object, 401
#
#         except User.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Invalid auth token!',
#                 'code': 401
#             }
#             return response_object, 401
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError as e:
#             print(e)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def get_logged_in_pharmacist(new_request):
#         try:
#             # get the auth token
#             auth_token = new_request.headers.get('Authorization')
#             if auth_token:
#                 resp = User.decode_auth_token(auth_token)
#                 if not isinstance(resp, str):
#                     adminId = ObjectId(resp['sub'])
#                     admin = Admin.objects.get({'_id': adminId})
#                     response_object = {
#                         'status': 'success',
#                         'data': {
#                             'adminId': admin._id,
#                             'email': admin.email,
#                             'admin': admin.role.roleName,
#                             # 'registered_on': str(user.registered_on)
#                         }
#                     }
#                     return response_object, 200
#
#                 response_object = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return response_object, 401
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'Invalid auth token.'
#                 }
#                 return response_object, 401
#
#         except Admin.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Invalid auth token!',
#                 'code': 401
#             }
#             return response_object, 401
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError as e:
#             print(e)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
#
#     @staticmethod
#     def get_logged_in_storeAdmin(new_request):
#         try:
#             # get the auth token
#             auth_token = new_request.headers.get('Authorization')
#             if auth_token:
#                 resp = Admin.decode_auth_token(auth_token)
#                 if not isinstance(resp, str):
#                     adminId = ObjectId(resp['sub'])
#                     admin = Admin.objects.get({'_id': adminId})
#                     response_object = {
#                         'status': 'success',
#                         'data': {
#                             'adminId': admin._id,
#                             'pharmacyId': admin.pharmacy,
#                             'email': admin.email,
#                             'admin': admin.role.roleName,
#                             # 'registered_on': str(user.registered_on)
#                         }
#                     }
#                     return response_object, 200
#
#                 response_object = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return response_object, 401
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'Invalid auth token.'
#                 }
#                 return response_object, 401
#
#         except Admin.DoesNotExist:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Invalid auth token!',
#                 'code': 401
#             }
#             return response_object, 401
#         except OSError as err:
#             print("OS error: {0}".format(err))
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry, Something went wrong.',
#                 'code': 500
#             }
#         except ValueError as e:
#             print(e)
#             print("Could not convert data to an integer.")
#         except:
#             print("Unexpected error:", sys.exc_info()[0])
#             print("Unexpected error:", sys.exc_info())
#             response_object = {
#                 'status': 'fail',
#                 'message': str(sys.exc_info()[1]),
#                 'code': 500
#             }
#             return response_object
