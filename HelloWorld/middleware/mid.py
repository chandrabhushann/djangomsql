import re
import json
import ast
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import requests
from django.core.exceptions import PermissionDenied
import base64
import json
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from jose import jwt, jws
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf import settings
from django.contrib.auth import authenticate , login

Users = get_user_model()

#AuthMiddleware.py
class APIGateway:
    def __init__(self, get_response):
        self.get_response = get_response
        #self.allowed_methods = ['get', 'post', 'put', 'delete']
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # self.auth(request)
        response = self.get_response(request)
        return response
        # Code to be executed for each request/response after
        # the view is called.
    

    def auth(self,request):
        return True
    

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        this function will be invoked before going to any views, so this function will work as a interceptor for any
        request being made to the platform so that the user can be verified and then passed to the relevant views if it
        is a valid user.
        :param request: request object
        """
        # if request.headers.get('Authorization',''):
        #     token = request.META.get('HTTP_AUTHORIZATION', False)
        #     token = token.replace('Bearer ','')
        #     #Need to discus with Arun regarding getting the secret information
        #     payload = jws.verify(token,  "chandra_secrets", algorithms=["HS256"])
        #     dict_val = ast.literal_eval(payload.decode('utf-8'))
        #     username =  dict_val.get('name',None)
        #     password = dict_val.get('password',None)
        #     user = authenticate(username=username,password=password)
        #     if user:
        #         login(request,user)     

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass