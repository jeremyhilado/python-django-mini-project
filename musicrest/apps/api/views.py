from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset

    serializer_class = ArtistSerializer

    def create(self, request):
        artist = Artist.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if artist:
            msg = 'Artist with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        artist = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user == artist.owner:
            raise PermissionDenied("You do not have permission to delete this artist")
        return super().destory(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        artist = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user == artist.owner:
            raise PermissionDenied(
                "You do not have permission to edit this artist"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicArtists(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Artist.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ArtistSerializer


class PublicArtistsDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Artist.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ArtistSerializer
