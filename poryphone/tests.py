from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Trainer
from .serializers import TrainerSerializer
from django.test import TestCase

# Create your tests here.

class BaseViewTest(APITestCase):
  client = APIClient()

  @staticmethod
  def create_trainer(name="", basepkmn=""):
    if name != "" and basepkmn != "":
      Trainer.objects.create(name=name, basepkmn=basepkmn)

  def setUp(self):
    #add test data
    self.create_trainer('Rosa', 'Snivy')
    self.create_trainer('Lt. Surge', 'Voltorb')
    self.create_trainer('Brendan', 'Treecko')

class GetAllTrainerTest(BaseViewTest):

  def test_get_all_trainer(self):
    """
    This test ensures that all sync pairs added in the setUp method
    exist when we make a GET request to the trainer/ endpoint
    """
    #hit the API endpoint
    response = self.client.get(
      reverse("trainer-all", kwargs={"version": "v1"})
    )

    #fetch the data from db
    expected = Trainer.objects.all()
    serialized = TrainerSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    
