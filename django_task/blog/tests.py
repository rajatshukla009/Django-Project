from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from.models import Post


class URLTests(SimpleTestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_name(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)

    def test_corrrect_template(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/home.html')

    def test_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_name(self):
        response = self.client.get(reverse('about-blog'))
        self.assertEqual(response.status_code,200)

    def test_corrrect_template(self):
        response = self.client.get(reverse('about-blog'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/about.html')


class PostTests(TestCase):

    @classmethod
    def setUp(cls):
        Post.objects.create(title="this is a test")

    def tests_text(self):
        post = Post.objects.get(id=1)
        expected_post_title = post.title
        self.assertEqual(expected_post_title,"this is a test")

    def test_post_list(self):
        response = self.client.get(reverse('posts'))
        self.assertEquals(response.status_code,200)
        self.assertContains(response, "this is a test")
        self.assertTemplateUsed(response,'blog/user_posts.html')
