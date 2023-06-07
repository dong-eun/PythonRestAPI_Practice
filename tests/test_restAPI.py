from testData.payloadData import PayloadData
from tests.BaseClass import BaseClass


class TestRestAPI(BaseClass):
  def test_can_create_task(self):
    # Create Task
    testData = PayloadData()
    payload = testData.new_task_payload()
    create_task_response = self.create_task(payload)
    assert create_task_response.status_code == 200

    # Get Task
    create_data = create_task_response.json()
    task_id = create_data["task"]["task_id"]
    get_task_response = self.get_task(task_id)
    assert get_task_response.status_code == 200

    # Verification json
    get_data = get_task_response.json()
    assert get_data["user_id"] == payload["user_id"]
    assert get_data["content"] == payload["content"]

  def test_can_update_task(self):
    testData = PayloadData()
    payload = testData.new_task_payload()

    # Create task
    create_task_response = self.create_task(payload)
    assert create_task_response.status_code == 200

    # Update task
    task_id = create_task_response.json()["task"]["task_id"]
    user_id = payload["user_id"]
    new_payload = {
      "content": "update content",
      "user_id": user_id,
      "task_id": task_id,
      "is_done": True
    }
    update_task_response = self.update_task(new_payload)
    assert update_task_response.status_code == 200

    # Get and Validate task
    get_task_response = self.get_task(task_id)
    assert get_task_response.status_code == 200
    get_data = get_task_response.json()
    assert get_data["content"] == new_payload["content"]
    assert get_data["is_done"] == new_payload["is_done"]

  def test_can_list_user(self):
    # Create N tasks
    testData = PayloadData()
    payload = testData.new_task_payload()
    for i in range(3):
      create_task_response = self.create_task(payload)
      assert create_task_response.status_code == 200

    # list tasks, and check that there are N items.
    user_id = payload["user_id"]
    list_task_response = self.list_task(user_id)
    assert list_task_response.status_code == 200
    list_task = list_task_response.json()["tasks"]
    assert len(list_task) == 3

  def test_can_delete_task(self):
    testData = PayloadData()
    payload = testData.new_task_payload()

    # Create task
    create_task_response = self.create_task(payload)
    assert create_task_response.status_code == 200

    # Delete the task
    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = self.delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get the task, and check that it's not found
    get_task_response = self.get_task(task_id)
    assert get_task_response.status_code == 404


