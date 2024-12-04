from rest_framework import serializers
from .models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id', 'title', 'singer']
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['singer']=Singer.objects.filter(id=instance.singer.id).values()
            return representation

class SingerSerializer(serializers.ModelSerializer):
    # songs=SongSerializer(read_only=True, many=True)
    class Meta:
        model=Singer
        fields=['id', 'name', 'gender','songs']
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['songs']=Song.objects.filter(id=instance.singer.id).values()
            return representation





# # class SingersSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model=Singer
# #         fields=['id', 'name', 'gender']

# class SongSerializer(serializers.ModelSerializer):
#     singer=SingerSerializer(read_only=True)
#     class Meta:
#         model=Song
#         fields=['id', 'title', 'singer']
    # #def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['singer']=Singer.objects.filter(id=instance.singer.id).values()
    #     return representation

# {
#         "id": 2,
#         "title": "Pani pani",
#         "singer": {
#             "id": 2,
#             "name": "Neha",
#             "gender": "F",
#             "songs": [----------------------------------
#                 2,         #nested serializer ka use krke aesa output ata hai  if u dont want this make new serializer of singer name change krdena
#                 7,
#                 8
#             ]--------------------------------
#         }
# },
        # "singer": {
#             "id": 2,
#             "name": "Neha",        this is what i am talking about or you can achieve this by to representation directly use krke purana wala serializer new ki koi need ni hai
#             "gender": "F"
#         }




# class SingerSerializer(serializers.ModelSerializer):
#     songs=serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#     # songs=serializers.StringRelatedField(read_only=True, many=True)
 
#     class Meta:
#         model=Singer
#         fields=['id', 'name', 'gender','songs']
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)    ## actually in singer table when we do instance.songs it is a queryset so how we can asscess a model object from query set so thats why dont use to_represention kyoki instance.object gives me query set
    #     representation['songs']=Song.objects.filter(instance.songs).values()

# class SingersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Singer
#         fields=['id', 'name', 'gender']

# class SongSerializer(serializers.ModelSerializer):
#     # singer=serializers.PrimaryKeyRelatedField(read_only=True)
#     # singer=SingerSerializer(read_only=True)
#     # singer=serializers.StringRelatedField(read_only=True)
#     class Meta: 
#         model=Song
#         fields=['id', 'title', 'singer']
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)    #read_only true hai tabbhi representation method chalta hai
#         representation['singer']=Singer.objects.filter(id=instance.singer.id).values()
#         return representation

# class SungsSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model=Song
#         fields=['id', 'title', 'singer']
















# class SongSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model=Song
#         fields=['id', 'title', 'singer']             #understanding to representation method
#     # def to_representation(self, instance):
#     #     rep = super().to_representation(instance)
#     #     rep['singer'] = Singer.objects.filter(id=instance.singer.id).values()
#     #     return rep


# class SingerSerializer(serializers.ModelSerializer):                                   ####[
#                                                                                         #    "name":"Neha"
#                                                                                         #    "gender":"F"
#     songs=SongSerializer(read_only=True, many=True)                                     #    "songs":[
#     class Meta:                                                                         #               {"id":1
#         model=Singer                                                                    #                "title:"pani pani"
#         fields=['id', 'name', 'gender','songs']                                         #                "singer":2                                           #    "id":2
#                                                                                         ####]

# class SingersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Singer            
#         fields=['id', 'name', 'gender']
                                                                                          

# class SongsSerializer(serializers.ModelSerializer):
#     singer=SingersSerializer(read_only=True)
#     class Meta:                                                   ##my out using Singer Serializer 
#         model= Song
#         fields=['id', 'title', 'singer']


# output using SingerSerializer for songs   /SONG/ api endpt     singer=SingerSerializer(read_only=True)
# [
#     {
#         "id": 2,
#         "title": "Pani pani",
#         "singer": {
#             "id": 2,
#             "name": "Neha",
#             "gender": "F",
            # "songs": [                                                ?
            #     {                                                     ?
            #         "id": 2,                                          ?
            #         "title": "Pani pani",                             ?
            #         "singer": [                                        ?       
            #             {                                              ? IDONT NEED THESE PART SO THATS WHY I WANT TO MAKE A NEW SERIALIZERS FOR SINGER 
            #                 "id": 2,                                   ?
            #                 "name": "Neha",                            ?
            #                 "gender": "F"                              ?
            #             }                                              ?
            #         ]                                                  ?
            #     }                                                      ?
            # ]                                                          ?
#         }
#     }
# ]

# output using singer=SingersSerializer(read_only=True)
# [
#     {
#         "id": 2,
#         "title": "Pani pani",
#         "singer": {
#             "id": 2,
#             "name": "Neha",
#             "gender": "F"
#         }
#     }
# ]

# [
#     {
#         "id": 2,
#         "title": "Pani pani",
#         "singer": {
#                 "id": 2,
#                 "name": "Neha",
#                 "gender": "F"
#             }
#     }
# ]