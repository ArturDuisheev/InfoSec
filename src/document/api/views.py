from rest_framework import generics
from document import models as doc_mod
from .serializers import DepartamentSerializer, DocumentSerializer


class DepartamentListAPIview(generics.ListAPIView):
    queryset = doc_mod.Departament.objects.all()
    serializer_class = DepartamentSerializer


class DocumentListAPIView(generics.ListAPIView):
    queryset = doc_mod.Document.objects.all()
    serializer_class = DocumentSerializer
