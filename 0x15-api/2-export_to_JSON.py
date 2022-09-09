#!/usr/bin/python3
"""From REST API export data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":

    mploy_nme = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(sys.argv[1])).json()
    num_done_tasks = 0
    total_num_tasks = 0
    task_title = {}
    task_title[mploy_nme["id"]] = []
    tdo_rqt = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for x in tdo_rqt:
        if x["userId"] == mploy_nme["id"]:
            total_num_tasks += 1
            if x["completed"] is True:
                num_done_tasks = True
            else:
                num_done_tasks = False
            task_title[mploy_nme["id"]]\
                .append({"task": x["title"], "completed": num_done_tasks,
                        "username": mploy_nme["username"]})

    with open("{}.json".format(mploy_nme["id"]), "w", encoding="utf8") as file:
        json.dump(task_title, file)
