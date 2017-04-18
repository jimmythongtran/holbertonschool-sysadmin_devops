#!/usr/bin/python3
"""
GET username and TODOs from https://jsonplaceholder.typicode.com
from employee ID
"""
import sys
import requests


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    empId = sys.argv[1]
    empName = requests.get("{}users/{}".format(api, empId)).json().get("name")

    totalTodos = 0
    doneTodos = []

    empTodos = requests.get("{}todos?userId={}".format(api, empId)).json()

    for toDo in empTodos:
        if toDo.get("userId") == int(empId):
            totalTodos += 1
            if (toDo.get("completed")):
                doneTodos.append(toDo.get("title"))

    print("Employee {:s} is done with tasks({:d}/{:d}):"
          .format(empName, len(doneTodos), totalTodos))

    for item in doneTodos:
        print("\t{:s}".format(item))
