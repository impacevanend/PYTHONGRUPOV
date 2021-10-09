from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from nogcodevapp.serializers.facturaSerializer import FacturaSerializer


class FacturaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)