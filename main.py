from linkedin import *

match = {
        "1": "Internship",
        "2": "Entry level",
        "3": "Associate",
        "4": "Mid-Senior level",
        "5": "Director",
        "6": "Executive"
    }


def init(**kwargs):
    login()
    search_jobs(**kwargs)
    save_jobs(**kwargs)


if __name__ == '__main__':
    print("Please enter job position you are looking for:")
    job_position = input()
    print("Please enter if you want remote job or not: (True/False)")
    remote_job = input()
    print("Please enter experience level (seperate by commas for multiple fields): \n 1. Internship\n 2. Entry level\n 3. Associate\n 4. Mid-Senior level\n 5. Director\n 6. Executive")
    experience_level = input().split(",")
    experience_level = [match[x.strip()] for x in experience_level]
    print("Please enter number of jobs you want to apply to (enter max for maximum number of jobs): ")
    jobs_num = input()
    if jobs_num == "max" or jobs_num == "Max" or (not jobs_num.isnumeric()):
        jobs_num = "max"
    else:
        jobs_num = int(jobs_num)
    init(search_key=job_position, remote=remote_job, easy_apply=True, experience_level=experience_level, number_of_jobs=jobs_num)
