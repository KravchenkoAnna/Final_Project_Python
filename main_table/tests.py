from django.test import TestCase
from .models import Concerts


class TestTableViews(TestCase):
    def test_query(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)


class TestConcertModel(TestCase):
    def setUp(self):
        self.concert = Concerts.objects.create(
            county="Sample Country",
            city="Sample City",
            month="Sample Month",
            week_day="Sample Week Day",
            day_number=25,
            #year=2025,
            address="Sample Address",
            exact_time="19:00:00"
        )

    def test_concerts_creation(self):
        self.assertTrue(isinstance(self.concert, Concerts))

        self.assertEqual(self.concert.county, "Sample Country")
        self.assertEqual(self.concert.city, "Sample City")
        self.assertEqual(self.concert.month, "Sample Month")
        self.assertEqual(self.concert.week_day, "Sample Week Day")
        self.assertEqual(self.concert.day_number, 25)
        self.assertEqual(self.concert.year, 1900)
        self.assertEqual(self.concert.address, "Sample Address")
        self.assertEqual(self.concert.exact_time, "19:00:00")

