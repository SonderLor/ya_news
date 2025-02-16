from unittest import skip
from news.models import News
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


@skip(reason="Test example")
class TestNews(TestCase):
    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )
        cls.user = User.objects.create(username='testUser')
        cls.user_client = Client()
        cls.user_client.force_login(cls.user)

    def test_successful_creation(self):
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    def test_title(self):
        self.assertEqual(self.news.title, self.TITLE)
