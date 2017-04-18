#!/usr/bin/python3
"""
GET username and TODOs from https://jsonplaceholder.typicode.com
from employee ID and export data in JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    empId = sys.argv[1]
    empName = requests.get("{}users/{}"
                           .format(api, empId)).json().get("username")
    empTodos = requests.get("{}users/{}/todos".format(api, empId)).json()

    todoList = []
    for toDo in empTodos:
        holder = {}
        holder["completed"] = toDo.get("completed")
        holder["toDo"] = toDo.get("title")
        holder["username"] = empName
        todoList.append(holder)

    with open("{}.json".format(empId), mode="w") as jsonFile:
        json.dump({empId: todoList}, jsonFile)
