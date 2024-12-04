# from django.shortcuts import render
from .models import*
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import*
from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token  #waise isko import krne ki need ni hai krto liye ho hi models me import and yha pe import* kiye to hai
from django.contrib.auth.models import User  #waise isko import krne ki need ni hai krto liye ho hi models me import and yha pe import* kiye to hai
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
# class product_variant(APIView):
#     def get(self, request, format=None): #pk=None
#         # id=pk
#         id=request.query_params.get('id')# id=pk  infronted data/query_params={'id':1}
#         if id:
#             try:
#                 product_variant=Product_variant.objects.get(id=id)
#                 serializer= Product_variantSerializer(product_variant)
#                 return Response(serializer.data)
#             except Product_variant.DoesNotExist:
#                 return Response({'msg':'product not exists'},status=status.HTTP_404_NOT_FOUND) 
#         product_variant=Product_variant.objects.all()
#         serializer=Product_variantSerializer(product_variant, many=True)
#         return Response(serializer.data)
 
# class product(APIView):
#     def get(self, request, format=None):#pk=None
#         # id=pk
#         id=request.query_params.get('id')
#         if id:
#             try:
#                 product=Product.objects.get(id=id)
#                 serializer=ProductSerializer(product)
#                 return Response(serializer.data)
#             except Product.DoesNotExists:
#                 return Response({'msg':'product nahi hai'},status=status.HTTP_404_NOT_FOUND)

#         product=Product.objects.all()
#         serializer=ProductSerializer(product, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def product_variant(request):#pk=None
    product=request.query_params.get('product')
    ram=request.query_params.get('ram')
    color=request.query_params.get('color')
    storage=request.query_params.get('storage')
    print(product, ram, color, storage)
    # product_variant=Product_variant.objects.get(product=product, color=color) error ayegi kyoki None aa rha hai color me value aa rhi hai but None ke hissab se koi model object hai ni db me
 
    if all([product, ram, color, storage]):
        #yha pe error aa sakti hai if product_variant exists hi na kare to yha pe filter laga lo kya product_variant exists krrha hai tab usko nikalo get se
        product_variant=Product_variant.objects.get( 
            product=product,
            color=color, 
            ram=ram,
            storage=storage
        )
        serializer=Product_variantSerializer(product_variant)
        return Response(serializer.data)
    if all([product, color, ram]):
        product_variant=Product_variant.objects.get(
            product=product,
            ram=ram, 
            color=color
        )
        serializer=Product_variantSerializer(product_variant)
        return Response(serializer.data)
    if all([product, color]):
        product_variant=Product_variant.objects.get(
            product=product,
            color=color, 
        )
        serializer=ProductvariantSerializer(product_variant)
        return Response({'data':serializer.data})
 
    if product:
        product_variant=Product_variant.objects.filter(product=product)  #get() returned more than one Product_variant -- it returned 2! becz in Product_variant table a product column has 1 do baar aa rha isliye ati hai ye eror
        serializer=Product_variantSerializer(product_variant, many=True)
        return Response({'data':serializer.data})
     


            

     
    
    


    
    # if all([]):
    # Using filter not get
    #if all([product, ram, color, storage]):
    #     product_variant=Product_variant.objects.filter(
    #         product=product,
    #         color=color, 
    #         ram=ram,                                        product_variant=[]
    #         storage=storage
    #     )
    #     serializer=Product_variantSerializer(product_variant, many=True)
    #     return Response(serializer.data)

    





































# class product_variant(APIView):
#     def get(self, request, format=None): #pk=None
#         # id=pk
#         id=request.query_params.get('id')# id=pk  infronted data/query_params={'id':1}
#         if id:
#             try:
#                 product_variant=Product_variant.objects.get(id=id)
#                 serializer= ProductsvariantSerializer(product_variant)
#                 return Response(serializer.data)
#             except Product_variant.DoesNotExist:
#                 return Response({'msg':'product not exists'},status=status.HTTP_404_NOT_FOUND) 
#         product_variant=Product_variant.objects.all()
#         serializer=ProductsvariantSerializer(product_variant, many=True)
#         return Response(serializer.data)
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]




















# from django.contrib.auth.hashers import check_password
# @api_view(['POST'])
# def loginapi(request):
#     username=request.data.get('username')
#     password=request.data.get('password')
#     if not username:
#         return Response({'msg':'please provide username'})
#     # if not password:
#     #     return Response({'msg':'please provide password'}) -->maine socha tha kuch
#     user=User.objects.get(username=username)   #username galat de dia than return invalid user name
#     if check_password (password, user.password):
#         serializer=UserSerializer(user)
#         token, create=Token.objects.get_or_create(user=user)
#         return Response(
#             {
#                 'token':token.key, 
#                 'data':serializer.data
#             }
#         )
#     return Response({'messasge':'invalid username or password'})



 

















































# ye bas implementation hai obtain_auth_token ki kaisa hoga wo
# def obtain_auth_token(request):
#     username=request.data.get('username')
#     password=request.data.get('password')
    
    
#     if not username:
#         return Response({'msg':'please provide username'})
#     elif User.objects.filter(username=username).exists():
#         user=User.objects.get(username=username)
#     else:
#         return Response({'non field errors':'Unable to log in with provided credentials.'})
#     if not password:
#         return Response({'msg':'please provide password'})
#     if check_password(password, user.password):
#         token, create=Token.objects.get_or_create(user=user)
#         return Response(
#             {
#                 'token':token.key
#             }
#         )
#     return Response({'non field errors':'Unable to log in with provided credentials.'})







# @api_view(['GET'])
# def product_variant(request): #pk=None
#     if request.method=='GET':
#         # id=pk
#         id=request.query_params.get('id')  #request.data.get data-->json data jo frontent se aa rha request.data laga ke usko python data meconvert krrhe thnku!!!! 
#         if id is not None:
#             if Product_variant.objects.filter(id=id).exists():
#                 product_variant=Product_variant.objects.get(id=id)
#                 serializer= Product_variantSerializer(product_variant)
#                 return Response(serializer.data)
#             else:
#                 res={'msg':'Student doesnot exists'}
#                 return Response(res)

#         product_variant=Product_variant.objects.all()
#         serializer=Product_variantSerializer(product_variant, many=True)
#         return Response(serializers.data) #{'data':serializer.data}


 



# @api_view(['GET'])
# def product(request):#pk
#     if request.method=='GET':
#         # id=pk
#         id=request.query_params.get('id')
#         if id:
#             if Product.objects.filter(id=id).exists():
#                 product=Product.objects.get(id=id)
#                 serializer=ProductSerializer(product)
#                 return Response(serializer.data)
#             else:
#                 return Response({'msg':'product nahi hai'},status=status.HTTP_404_NOT_FOUND)

#         product=Product.objects.all()
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
