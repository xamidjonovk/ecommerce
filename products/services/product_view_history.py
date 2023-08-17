from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductViewHistory
from products.serializers import ProductViewHistorySerializer
from drf_yasg.utils import swagger_auto_schema


class ProductViewHistoryCreate(APIView):
    serializer_class = ProductViewHistorySerializer

    @swagger_auto_schema(request_body=ProductViewHistorySerializer)
    def post(self, request):
        serializer = ProductViewHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
