import pytest
import os

from criteo_api_marketingsolutions_v2021_10.configuration import Configuration
from criteo_api_marketingsolutions_v2021_10.api.gateway_api import GatewayApi
from criteo_api_marketingsolutions_v2021_10.api_client import ApiClient
from criteo_api_marketingsolutions_v2021_10.rest import ApiException

class TestGatewayApi:
  @pytest.fixture(autouse=True)
  def before_each(self):
    self.client_id = os.environ.get("TEST_CLIENT_ID")
    self.client_secret = os.environ.get("TEST_CLIENT_SECRET")
    self.application_id = int(os.environ.get("TEST_APPLICATION_ID"))
  
    self.client = ApiClient(Configuration(username=self.client_id, password=self.client_secret))

  def test_environment_variables(self):
    assert len(self.client_id) > 0, "Environment variable \"TEST_CLIENT_ID\" not found."
    assert len(self.client_secret) > 0, "Environment variable \"TEST_CLIENT_SECRET\" not found."
    assert self.application_id > 0, "Environment variable \"TEST_APPLICATION_ID\" not found."

  def test_get_current_application_should_succeed_with_valid_token(self):
    # Arrange
    api = GatewayApi(self.client)

    # Act
    http_response = api.get_current_application()

    # Assert
    assert self.application_id == http_response.data.attributes.application_id


  def test_get_current_application_should_succeed_with_renewed_invalid_token(self):
      # Arrange
      invalid_token = "invalid.access.token"
      self.client.configuration.access_token = invalid_token
      api = GatewayApi(self.client)

      # Act
      http_response = api.get_current_application()

      # Assert
      assert self.application_id == http_response.data.attributes.application_id


  def test_get_current_application_should_fail_without_token(self):
    # Arrange
    api = GatewayApi(ApiClient())

    # Act
    try:
      api.get_current_application()

    # Assert
    except ApiException as exception:
      assert exception.status == 401
