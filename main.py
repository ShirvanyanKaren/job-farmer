from linkedin import *
from questions import menu

def init(**kwargs):
    login()
    search_jobs(**kwargs)
    save_jobs(**kwargs)


if __name__ == '__main__':
    answers = menu()
    init(**answers)
    
