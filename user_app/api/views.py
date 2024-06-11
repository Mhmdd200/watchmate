from user_app.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.api.models import create_auth_token

@api_view (['POST',])
def registration_views(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            account = serializer.save()
            data['response'] = "It is succesfully done!"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user = account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)