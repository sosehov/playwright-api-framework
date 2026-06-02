from faker import Faker

fake = Faker()

class UserFactory:
  
  @staticmethod
  def valid_user():
    return {
    "name": fake.name(),
    "job": fake.job()
    }
