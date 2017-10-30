from rest_framework import serializers
from mrbelvedereci.api.serializers.repository import RepositorySerializer
from mrbelvedereci.plan.models import Plan
from mrbelvedereci.repository.models import Repository

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    repo = RepositorySerializer(read_only=True)
    repo_id = serializers.PrimaryKeyRelatedField(
        queryset=Repository.objects.all(),
        source='repo',
        write_only=True
    )
    class Meta:
        model = Plan
        fields = (
            'id',
            'active',
            'context',
            'description',
            'flows',
            'name',
            'org',
            'public',
            'repo',
            'repo_id',
            'regex',
            'type',
        )