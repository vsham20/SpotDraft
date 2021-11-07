from django.http import Http404
from rest_framework import filters
from rest_framework import mixins, generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
from .models import Planets, Movies
from .serializers import PlanetsSerializer, MoviesSerializer


class MoviesView(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ViewSets define the view behavior.
class PlanetsView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Planets.objects.all()
    serializer_class = PlanetsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FavoritesView(viewsets.ViewSet):
    valid_obj_types = {
        "movies": (Movies, MoviesSerializer),
        "planets": (Planets, PlanetsSerializer)
    }

    def get_object(self, pk, model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, obj, pk, format=None):
        if obj not in FavoritesView.valid_obj_types.keys():
            return Response(status=status.HTTP_404_NOT_FOUND)
        model, serializer_class = FavoritesView.valid_obj_types[obj]
        queryset = self.get_object(pk, model)
        serializer = serializer_class(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritesMovieView(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = MoviesSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
