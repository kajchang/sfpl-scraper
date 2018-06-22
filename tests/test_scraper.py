import unittest
import os
import codecs

from bs4 import BeautifulSoup
import sfpl


class TestScraper(unittest.TestCase):
    def test_holds(self):
        with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mockups/holds.html'), encoding='utf-8') as mockup:
            result = sfpl.SFPL.parseHolds(
                BeautifulSoup(mockup.read(), 'html.parser'))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Fundamentals of Deep Learning')
        self.assertEqual(result[0].author.name, 'Buduma, Nikhil')
        self.assertEqual(result[0].version, {'Book': 2017})
        self.assertEqual(result[0].status, 'Pickup by:  Jun 18, 2018')
        self.assertEqual(
            result[0].subtitle, 'Designing Next-generation Machine Intelligence Algorithms')
        self.assertEqual(result[0].id, 3388519093)

    def test_checkouts(self):
        with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mockups/checkouts.html'), encoding='utf-8') as mockup:
            result = sfpl.SFPL.parseCheckouts(
                BeautifulSoup(mockup.read(), 'html.parser'))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Basics of Web Design')
        self.assertEqual(result[0].author.name, 'Felke-Morris, Terry')
        self.assertEqual(result[0].version, {'Book': 2012})
        self.assertEqual(result[0].status, 'Due Jun 28, 2018')
        self.assertEqual(result[0].subtitle, 'HTML5 & CSS3')
        self.assertEqual(result[0].id, 2423174093)

    def test_shelf(self):
        with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mockups/shelf.html'), encoding='utf-8') as mockup:
            result = sfpl.SFPL.parseShelf(
                BeautifulSoup(mockup.read(), 'html.parser'))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Bitcoin')
        self.assertEqual(result[0].author.name, 'United States')
        self.assertEqual(result[0].version, {'Website or Online Data': 2014})
        self.assertEqual(
            result[0].subtitle, 'Examining the Benefits and Risks for Small Business : Hearing Before the Committee on Small Business, United States House of Representatives, One Hundred Thirteenth Congress, Second Session, Hearing Held April 2, 2014')
        self.assertEqual(result[0].id, 2776977093)

    def test_author(self):
        author = sfpl.Author('J.K. Rowling')
        result = author.getBooks()

        self.assertEqual(len(result), 5)
        self.assertEqual(
            result[0].title, "Harry Potter and the Sorcerer's Stone")
        self.assertEqual(result[0].author.name, 'Rowling, J. K.')
        self.assertEqual(result[0].version, {'Book': 1997, 'Large Print': 1999,
                                             'Audiobook CD': 1999, 'Downloadable Audiobook': 2012, 'eBook': 2012})

    def test_book(self):
        book = sfpl.Book("Harry Potter and the Sorcerer's Stone", 'Rowling, J. K.', {
                         'Book': 1997, 'Large Print': 1999, 'Audiobook CD': 1999, 'Downloadable Audiobook': 2012, 'eBook': 2012}, None, 3023751093)

        self.assertEqual(book.getDetails(), {'Publisher': 'New York, NY : Scholastic, Incorporated, 2015', 'Edition': 'First illustrated edition', 'ISBN': [
                         '9780545790352', '0545790352'], 'Call Number': 'jF ROWL', 'Characteristics': '246 p. : col. ill. ; 28 cm', 'Additional Contributors': 'Kay, Jim   - Illustrator'})
