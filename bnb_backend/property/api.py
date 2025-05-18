from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework_simplejwt.tokens import AccessToken
# from .forms import PropertyForm
from .models import Property
from .serializers import PropertiesListSerializers

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializers(properties,many=True)
    
    return JsonResponse({
        'data':serializer.data
    })