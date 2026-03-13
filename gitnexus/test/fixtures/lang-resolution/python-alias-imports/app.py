from models import Repo as R
from models import User as U


def main():
    u = U("alice")
    r = R("https://example.com")
    u.save()
    r.persist()
