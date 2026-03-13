from models import Repo, User


def main():
    user = User()
    user.save()

    repo = Repo()
    repo.persist()
