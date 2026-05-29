import uuid

class UserFactory:
  
  @staticmethod
  def create_user():
    return {
      "name": f"user_{uuid.uuid4().hex[:6]}",
      "job": "QA Engineer"
    }