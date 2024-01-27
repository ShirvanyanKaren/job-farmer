from linkedin import *


def init(**kwargs):
    login()
    search_jobs(**kwargs)
    save_jobs()


init(search_key="Web Developer", remote=True, easy_apply=True)
