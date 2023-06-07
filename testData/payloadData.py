import uuid


class PayloadData:
  def new_task_payload(self):
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    payload = {
      "content": content,
      "user_id": user_id,
      "is_done": False
    }
    return payload