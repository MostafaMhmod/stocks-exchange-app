
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from thndr.serializers.user_serializer import UserRetreieveSerializer
from django.contrib.auth.models import User


@api_view(["POST"])
def user(request):
    user_id = request.data.get('user_id')
    try:
        queryset = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise NotFound

    serializer = UserRetreieveSerializer(queryset)

    return Response(serializer.data)
