from rest_framework import serializers
from apps.api.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'biography', 'created_at',
                  'updated_at', 'owner', 'is_public')
