from repo import Repo
from user import User


def process_entities():
    user: User = User()
    repo: Repo = Repo()
    user.save()
    repo.save()
