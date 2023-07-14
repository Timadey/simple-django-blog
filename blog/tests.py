from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


# Create your tests here.
class TestPostModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser", email="testuser@email.com", password="secret"
        )
        self.post = Post.objects.create(
            title="First test post",
            content="The content for the first test post",
            author=self.user,
        )

    def test_string_representation(self):
        return self.assertEqual(self.post.title, str(self.post.title))

    def test_homepage_reponse(self):
        resp = self.client.get("")
        reverse_resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(reverse_resp.status_code, 200)
        self.assertContains(resp, self.post.title)
        self.assertTemplateUsed("home.html")

    def test_post_details_response(self):
        resp = self.client.get("/post/1")
        no_resp = self.client.get("post/111111111111111")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertTemplateUsed("post_details.html")

    def test_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), "/post/1")

    def test_post_create(self):
        resp = self.client.post(
            reverse("post_create"),
            {
                "title": "Test new post title",
                "content": "The content of the new test post",
                "author": "Test Author",
            },
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Test new post title")
        self.assertContains(resp, "The content of the new test post")
        self.assertTemplateUsed(resp, "post_create.html")

    def test_post_update(self):
        resp = self.client.post(
            reverse("post_edit", args=[1]),
            {
                "title": "[Edited] First Post",
                "content": "[Edited] content of the first post",
                "author": "Edited Author",
            },
        )
        edited_post = Post.objects.get(id = 1)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(edited_post.title, "[Edited] First Post")
        self.assertEqual(edited_post.content, "[Edited] content of the first post")
        self.assertNotEqual(edited_post.author, "Edited Author")

    def test_post_delete(self):
        resp = self.client.post(reverse("post_delete", args=[1]))
        no_resp = self.client.get(reverse("post_detail", args=[1]))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(no_resp.status_code, 404)