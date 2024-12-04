from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Singer, Song
from .serializers import SongSerializer, SingerSerializer #SongSerializer SungsSerializer #SongsSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# -----------------------------------------------------------
# path('singer/', views.singer)
# path('singer/<int:pk>', views.singer),
# @api_view(['GET', 'POST', 'PUT'])
# def singer(request, pk=None):
#     if request.method == 'GET':
#         id=pk
#         if id is not None:
#             singer=Singer.objects.get(id=id)
#             serializer=SingerSerializer(singer)
#             return Response(serializer.data)
#         singer=Singer.objects.all()
#         serializer=SingerSerializer(singer, many=True)
#         return Response(serializer.data)
    
# path('singer/', views.singer) 
# @api_view(['GET'])
# def singer(request):
#     print(request.data) 
#     id=request.query_params.get('id')
#     if id:
#         if Singer.objects.filter(id=id).exists():
#             singer=Singer.objects.get(id=id)
#             serializer=SingerSerializer(singer)
#             return Response(serializer.data)
#     return Response({'msg': 'mass'})
    # singer=Singer.objects.all()
    # serializer=SingerSerializer(singer, many=True)
    # return Response(serializer.data)


    
    
    
    
    
    
    # if request.method == 'POST':
    #     serializer=SingerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg':'Data inserted'}
    #         return Response(res)
    #     return Response(serializer.errors)
    
    # if request.method == 'PUT':
    #     id=pk
    #     singer=Singer.objects.get(id=id)
    #     serializer=SingerSerializer(singer,request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg':'data updated'}
    #         return Response(res)
    #     return Response(serializer.errors)


# ----------------------------------------------------------------


class SINGER(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            singer=Singer.objects.get(id=id)
            serializer=SingerSerializer(singer)
            return Response(serializer.data)
        singer=Singer.objects.all()
        serializer=SingerSerializer(singer, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer=SingerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg':'Data inserted'}
    #         return Response(res)
    #     return Response(serializer.errors)
    
    # def put(self, request, pk, format=None):
    #     id=pk
    #     singer=Singer.objects.get(id=id)
    #     serializer=SingerSerializer(singer,request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg':'data updated'}
    #         return Response(res)
    #     return Response(serializer.errors)
    
    # def delete(self, request, pk, format=None):
    #     id=pk
    #     singer = Singer.objects.get(id=id)
    #     singer.delete()
    #     res={"msg":"Data deleted"} 
    #     return Response(res)
    
# class SINGER(APIView):
#     def get(self, request, pk=None, format=None):
#         id=pk
#         if id is not None:
#             singer=Singer.objects.get(id=id)
#             serializer=SingerSerializer(singer)
#             return Response(serializer.data)
#         singer=Singer.objects.all()
#         serializer=SingerSerializer(singer, many=True)
#         return Response(serializer.data)
    

class SONG(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id :
            song=Song.objects.get(id=id)
            serializer=SongSerializer(song)              #SongsSerializer ka use kia hai na ki song
            return Response(serializer.data)
        song=Song.objects.all()
        serializer=SongSerializer(song, many=True)
        return Response(serializer.data)

# class SONG(APIView):
#     def get(self, request, pk=None, format=None):
#         id=pk
#         if id :
#             song=Song.objects.get(id=id)
#             serializer=SongSerializer(song)
#             return Response(serializer.data)
#         song=Song.objects.all()
#         serializer=SongSerializer(song, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer=SungsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data inserted'}
#             return Response(res)
#         return Response(serializer.errors)
    
#     def put(self, request, pk, format=None):
#         id=pk
#         song=Song.objects.get(id=id)
#         serializer=SungsSerializer(song, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data updated'}
#             return Response(res)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk, format=None):
#         id=pk
#         song=Song.objects.get(id=id)
#         song.delete()
#         res={"msg":"Data deleted"}
#         return Response(res)







     
        
        





