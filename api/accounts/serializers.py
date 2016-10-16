from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='user-detail')
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'link', 'email', 'date_joined', 'is_staff',
                  'is_superuser', 'is_active', 'first_name', 'last_name',
                  'password',)
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        """Create the object"""
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
