from base.serializers import BaseSerializer

from document import models as doc_mod


class DepartamentSerializer(BaseSerializer):
    class Meta:
        model = doc_mod.Departament
        fields = (
            'ID',
            'title',
            'slug',
            'created_at',
            'updated_at'
        )


class DocumentSerializer(BaseSerializer):
    class Meta:
        model = doc_mod.Document
        fields = (
            'ID',
            'number',
            'name',
            'document',
            'departament',
            'created_at',
            'updated_at'
        )
