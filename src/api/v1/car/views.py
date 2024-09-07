from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from src.api.auth.permissions import IsOwnerOrReadOnlyAndCreate
from src.apps.car.models import Car
from src.apps.car.serializers import CarSerializer
from src.apps.comment.models import Comment
from src.apps.comment.serializers import CommentSerializer


class CarViewSet(viewsets.ViewSet):
    """
    VewSet для сущности "Автомобиль", методы: list, retrieve, create, destroy, update, create_comment, get_comments
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyAndCreate)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def create(self, request):
        request.data["owner"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)

        self.check_object_permissions(request, instance)

        request.data["owner"] = request.user.id
        serializer = self.serializer_class(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)

        self.check_object_permissions(request, instance)

        instance.delete()
        return Response(None)

    @action(detail=True, methods=["get", "post"], url_path="comments")
    def comments(self, request, pk=None):
        if request.method == "GET":
            comments = get_object_or_404(self.queryset, pk=pk).comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            get_object_or_404(self.queryset, pk=pk)
            request.data["car"] = pk
            request.data["author"] = request.user.id
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)
