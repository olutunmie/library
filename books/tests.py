from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A book title",
            subtitle="based on a subtitle",
            author="Random Author",
            isbn="1234567890123"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A book title")
        self.assertEqual(self.book.subtitle, "based on a subtitle")
        self.assertEqual(self.book.author, "Random Author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "based on a subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")