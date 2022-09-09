#!/usr/bin/python3
"""From REST API export data in the CSV format"""

import csv
import requests
import sys


if __name__ == "__main__":

    mploye_nme = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                              .format(sys.argv[1])).json()
    num_done_tasks = 0
    total_num_tasks = 0
    task_title = []
    tdo_rqt = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for x in tdo_rqt:
        if x["userId"] == mploye_nme["id"]:
            total_num_tasks += 1
            if x["completed"] is True:
                num_done_tasks = True
            else:
                num_done_tasks = False
            task_title.append([mploye_nme["id"], mploye_nme["username"],
                              num_done_tasks, x["title"]])

    with open("{}.csv".format(mploye_nme["id"]), "w", encoding="utf8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(task_title)
