
from rest_framework import generics

from app_copy.models import Copy
from app_copy.serializers import CopySerializer
from drf_spectacular.utils import extend_schema


class CopyView(generics.ListCreateAPIView):
    queryset =  Copy.objects.all()
    serializer_class = CopySerializer

    @extend_schema(
        operation_id="copies_get",
        description="Rota de listagem de cópias cadastrados.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="copy_post",
        description="Rota de cadastro de cópia.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    @extend_schema(
        operation_id="copy_get",
        description="Rota de listagem de uma cópia específica.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="copy_patch",
        description="Rota para atualização de dados de uma cópia específica.",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="cópia_delete",
        description="Rota para deleção de uma cópia específica.",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)