#!/usr/bin/python3
"""From REST API export data in the JSON format"""

import json
import requests


if __name__ == "__main__":

    mply = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    num_done_tasks = 0
    total_num_tasks = 0
    task_title = {}
    tdo_rqt = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for x in mply:
        task_title[x["id"]] = []
        for y in tdo_rqt:
            if y["userId"] == x["id"]:
                task_title[x["id"]]\
                    .append({"username": x["username"], "task": y["title"],
                            "completed": y["completed"]})

    with open("todo_all_employees.json", "w", encoding="utf8") as file:
        json.dump(task_title, file)
