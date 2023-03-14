from django.contrib.auth.backends import BaseBackend
from django.db import connection

from drauto.models import Client

from django.contrib.auth.backends import BaseBackend


class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, user_type=None, **kwargs):
        try:
            user = Client.objects.get(client_name=username)

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT dbo.ValidateLogin('{username}', '{password}', '{user_type}')")
                result = cursor.fetchone()[0]
                if result == True:
                    return user
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None
