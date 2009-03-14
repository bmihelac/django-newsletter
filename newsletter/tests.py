r"""
>>> from newsletter.models import *
>>> subscription = Subscription(email="testemail@example.com")
>>> subscription.save()
>>> subscription.newsletter_groups.all()
[]

# Create Newsletter Group
>>> ng = NewsletterGroup(name = "media")
>>> ng.save()
>>> subscription.newsletter_groups.add(ng)
>>> subscription.newsletter_groups.all()
[<NewsletterGroup: media>]
"""

from django.test import TestCase
from django.core.urlresolvers import reverse


class ClientTest(TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_user_subscribe_twice_should_not_throw_error(self):
        post_data = {'email': "test@example.com", 'subscribed': True}
        for i in range(2):
            response = self.client.post(reverse('subscribe_detail'), post_data)
            self.assertTemplateUsed(response, "newsletter/success.html")

        