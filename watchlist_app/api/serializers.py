from watchlist_app.models import Watchlist,StreamPlatform,Review
from rest_framework import serializers # type: ignore
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Watchlist
        fields = "__all__"
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

'''   class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators = [name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
'''
    
    