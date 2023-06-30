from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
User = get_user_model()

import logging

logger = logging.getLogger("django.request")
logging.warning("WARNING: core.serializer : logging is active")

class UserAvatarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)
    