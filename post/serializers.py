from rest_framework import serializers
from .models import Post

import logging

logger = logging.getLogger("django.request")
logging.warning("WARNING: post.serializer : logging is active")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

