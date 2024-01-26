from linkedin import *


def init(**kwargs):
    try:
        login()
        search_jobs(**kwargs)
    except Exception as e:
        print(f'An error occurred: {e}')


init(search_key="Web Developer", remote=True, easy_apply=True)
