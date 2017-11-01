from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategorySerializer
from product.models import Category
# Create your views here.


class CategoryApi(APIView):
    serializer_class = CategorySerializer

    def get(self, request):

        if request.user.is_authenticated:
            serializer = self.serializer_class (Category.objects.all () , many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'failed': 'Permissão negada.'}, status=status.HTTP_403_FORBIDDEN)