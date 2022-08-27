from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(text='testing text')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        self.assertEqual(f'{post.text}', 'testing text')


class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        post=Post.objects.create(text='Bekzod Karimov')

    def test_view_url_exists(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'posts/index.html')

