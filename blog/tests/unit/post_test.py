# every time we create a test, we construct it as an object that inherits from other class


# importing class to inherit from
from unittest import TestCase
# importing class to test
from post import Post


class PostTest(TestCase):
    # always start with def test_!
    def test_create_post(self):
        p = Post('Test', 'Test content')
        # Check if str='Test' is equal to title of p
        self.assertEqual('Test', p.title)
        # same for content property
        self.assertEqual('Test content', p.content)

