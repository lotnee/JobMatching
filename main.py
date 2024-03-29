
from pathlib import Path
from utils import utils
import time


def main():

    try:
        print("Getting csvs data")
        jobs_list = utils.get_csvs(Path("data/jobs.csv"))
        job_seeker_list = utils.get_csvs(Path("data/jobseekers.csv"))
    except FileNotFoundError as e:
        print(f'Something went wrong when trying to load the csvs: {e}')
        exit()
    print("Setting up Job and job seeker objects")
    jobs_obj_list = utils.setup_object("Job", jobs_list)
    job_seekers_obj_list = utils.setup_object("Job Seeker", job_seeker_list)

    print("Generating Output")
    job_match_obj_list = utils.setup_job_match(job_seeker_list=job_seekers_obj_list, job_list=jobs_obj_list)
    job_recommendations = utils.create_output(job_match_list=job_match_obj_list)

    job_recommendations.to_csv("results/result.csv", sep=",", index=False, encoding="utf-8")



if __name__ == "__main__":
    main()