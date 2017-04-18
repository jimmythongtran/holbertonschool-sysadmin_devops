#!/usr/bin/python3
"""
GET username and TODOs from https://jsonplaceholder.typicode.com
from employee ID and export data in CSV format
"""
import sys
import requests
import csv


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    empId = sys.argv[1]
    empName = requests.get("{}users/{}"
                           .format(api, empId)).json().get("username")
    empTodos = requests.get("{}users/{}/todos".format(api, empId)).json()

    filename = "{}.csv".format(sys.argv[1])

    with open("{}.csv".format(empId), mode="w") as csvFile:
        writer = csv.writer(csvFile, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for toDo in empTodos:
            holder = [empId, empName, toDo.get("completed"),
                      toDo.get("title")]
            writer.writerow(holder)
