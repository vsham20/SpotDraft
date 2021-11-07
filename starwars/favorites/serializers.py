from rest_framework import serializers

from .models import Planets, Movies


class PlanetsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    custom_name = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()
    url = serializers.SerializerMethodField()
    is_favorite = serializers.BooleanField(default=False)

    class Meta:
        model = Planets
        fields = ('__all__')

    def get_url(self, obj):
        return "https://swapi.dev/api/planets/{}".format(obj.pk)

class MoviesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    custom_title = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()
    release_date = serializers.DateField()
    url = serializers.SerializerMethodField()
    is_favorite = serializers.BooleanField(default=False)

    class Meta:
        model = Movies
        fields = ('__all__')

    def get_url(self, obj):
        return "https://swapi.dev/api/films/{}".format(obj.pk)
