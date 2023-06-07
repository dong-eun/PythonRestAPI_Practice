import pytest
import requests

@pytest.fixture(scope="class")
def setup(request):
  ENDPOINT = "https://todo.pixegami.io"

  request.cls.ENDPOINT = ENDPOINT
