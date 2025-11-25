from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def validate_comment(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O comentário deve ter no máximo 200 caracteres.')
        return value