from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=True)
    release_date = serializers.CharField(max_length=200)
    game_category = serializers.CharField(max_length=False)
    played = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)




        #>>>>>>>>>>>>>> MISSPELLED player
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance