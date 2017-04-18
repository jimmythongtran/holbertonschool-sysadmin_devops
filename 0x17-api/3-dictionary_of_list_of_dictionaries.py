#!/usr/bin/python3
"""
GET username and TODOs from https://jsonplaceholder.typicode.com
from employee ID and export data in JSON format for all employees
"""
import json
import requests


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    allUsers = requests.get("{}users".format(api)).json()
    empTodos = requests.get("{}todos".format(api)).json()

    records = {}
    for user in allUsers:
        empId = user.get("id")
        empName = user.get("username")
        todoList = []

    for toDo in empTodos:
        holder = {}
        holder["completed"] = toDo.get("completed")
        holder["toDo"] = toDo.get("title")
        holder["username"] = empName
        todoList.append(holder)

    records[empId] = todoList
    with open("todo_all_employees.json", mode="w") as jsonFile:
        json.dump(records, jsonFile)
