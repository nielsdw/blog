from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.serializers import BlogSerializer, BlogListSerializer, BlogPatchSerializer
from blog.models import Blog
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404


class Blogs(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug=None):
        if slug is not None:
            queryset = get_object_or_404(Blog, slug=slug)
            serializer = BlogSerializer(queryset)
            return Response(serializer.data)
        else:
            queryset = Blog.objects.all()
            serializer = BlogListSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.initial_data["slug"] = slugify(serializer.initial_data["title"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)

    def patch(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogPatchSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        blog.delete()
        return Response()
