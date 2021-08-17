import sys
import requests
from flask_ades_wpst.sqlite_connector import sqlite_get_procs, sqlite_deploy_proc, sqlite_get_proc, sqlite_undeploy_proc

def proc_dict(proc):
    return {"id": proc[0],
            "title": proc[1],
            "abstract": proc[2],
            "keywords": proc[3],
            "owsContextURL": proc[4],
            "processVersion": proc[5],
            "jobControlOptions": proc[6].split(','),
            "outputTransmission": proc[7].split(','),
            "immediateDeployment": str(bool(proc[8])).lower(),
            "executionUnit": proc[9]}

def get_procs():
    saved_procs = sqlite_get_procs()
    procs = [proc_dict(saved_proc) for saved_proc in saved_procs]
    return procs

def get_proc(proc_id):
    proc_desc = sqlite_get_proc(proc_id)
    return proc_dict(proc_desc)

def deploy_proc(app_desc_url):
    response = requests.get(app_desc_url)
    if response.status_code == 200:
        proc_spec = response.json()
        sqlite_deploy_proc(proc_spec)
    return proc_spec
            
def undeploy_proc(proc_id):
    proc_desc = sqlite_undeploy_proc(proc_id)
    return proc_dict(proc_desc)

def get_jobs():
    jobs = ["job1", "job2", "job3"]
    return jobs

def get_job(proc_id, job_id):
    # Required fields in job_info response dict:
    #   jobID (str)
    #   status (str) in ["accepted" | "running" | "succeeded" | "failed"]
    # Optional fields:
    #   expirationDate (dateTime)
    #   estimatedCompletion (dateTime)
    #   nextPoll (dateTime)
    #   percentCompleted (int) in range [0, 100]
    job_info = {"jobID": job_id, "status": "running"}
    return job_info

def exec_job(inputs, outputs, mode, response):
    job_id = "job5"
    status_url = "https://myhost/status/{}".format(job_id)
    return status_url
            
def dismiss_job(proc_id, job_id):
    job_status = "canceled" # what string to use here?
    dismiss_status = {"jobID": job_id, "status": job_status}
    return dismiss_status

def get_job_results(proc_id, job_id):
    job_results = ["file:///path/to/result1",
                   "file:///path/to/result2"]
    return job_results
