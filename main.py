from linkedin import *


def init(**kwargs):
    job_ids = []
    try:
        login()
        search_jobs(**kwargs)
        get_job_ids()
    except Exception as e:
        print(f'An error occurred: {e}')


init(search_key="Web Developer", remote=True, easy_apply=True)
