from rest_framework import serializers
from saravanan.models import Saravanan


class SaravananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saravanan
        fields = (
            'id',
            'avName',
            'avlUsers',
            'avlYears',
            'avlKey',
            'avlEmail',
            'avAgent',
            'avActivated',
            'avClient',
            'avExpiry'
        )
