from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter


@api_view(['GET', "POST"])
def news_list(request):
    if request.method == "GET":
        obj = News.objects.all()
        serializer = NewsSerializer(obj, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = NewsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class ListFilter(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['headline', 'news_authors']

