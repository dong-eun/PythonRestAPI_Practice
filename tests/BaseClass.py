import pytest
import requests


@pytest.mark.usefixtures('setup')
class BaseClass():
  def create_task(self, payload):
    return requests.put(self.ENDPOINT + "/create-task", json=payload)

  def update_task(self, payload):
    return requests.put(self.ENDPOINT + "/update-task", json=payload)

  def get_task(self, task_id):
    return requests.get(self.ENDPOINT + f"/get-task/{task_id}")

  def list_task(self, user_id):
    return requests.get(self.ENDPOINT + f"/list-tasks/{user_id}")

  def delete_task(self, task_id):
    return requests.delete(self.ENDPOINT + f"/delete-task/{task_id}")