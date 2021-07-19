import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from blog.models import Blog


@pytest.mark.django_db()
class Tests:
    def setup(self):
        self.client = APIClient()
        User.objects.create_user(username="foo", password="bar")
        response = self.client.post(
            "/api/token/", {"username": "foo", "password": "bar"}, format="json"
        )
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + response.data["access"])

    def test_get_jwt(self):
        client = APIClient()
        response = client.post(
            "/api/token/", {"username": "foo", "password": "bar"}, format="json"
        )
        assert response.status_code == 200
        assert response.data["access"] is not None
        access = response.data["access"]
        assert response.data["refresh"] is not None

        response = client.get("/blogs")
        assert response.status_code == 401

        client.credentials(HTTP_AUTHORIZATION="Bearer " + access)

        response = client.get("/blogs")
        assert response.status_code == 200

    def test_post_blog(self):
        response = self.client.post(
            "/blogs",
            {"title": "foo", "summary": "bar", "content": "qaz"},
            format="json",
        )
        assert response.status_code == 201  # Created
        blog = Blog.objects.first()
        assert blog is not None

        response = self.client.get("/blogs/" + blog.slug)
        assert response.status_code == 200

    def test_get_all_blogs(self):
        response = self.client.get("/blogs")
        assert response.status_code == 200

    def test_patch_blog(self):
        blog = Blog.objects.create(
            title="title", slug="title", summary="summary", content="content"
        )
        blog.save()
        response = self.client.patch(
            "/blogs/" + blog.slug,
            {"title": "title", "content": "content", "summary": "some other summary"},
            format="json",
        )
        assert response.status_code == 200
        blog.refresh_from_db()
        assert blog.summary == "some other summary"
        response = self.client.patch("/blogs/a" + blog.slug)  # some non-existent slug
        assert response.status_code == 404

    def test_delete_blog(self):
        blog = Blog.objects.create(
            title="title", slug="title", summary="summary", content="content"
        )
        blog.save()
        assert Blog.objects.count() == 1
        self.client.delete("/blogs/" + blog.slug)
        assert Blog.objects.count() == 0
