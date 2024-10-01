import logging
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

logger = logging.getLogger(__name__)


class GettingDataTestCase(APITestCase):

    def get_document(self):
        url = reverse('doc-list')
        response = self.client.get(path=url, content_type='application/json')
        logger.error(f"Response data {response.data}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
