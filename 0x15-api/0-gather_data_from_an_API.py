#!/usr/bin/python3
"""From REST API returns information about his/her TODO list progress"""

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
                task_title.append("\t" + " " + x["title"])
                num_done_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(mploye_nme['name'], num_done_tasks, total_num_tasks))
    print('\n'.join(task_title))
