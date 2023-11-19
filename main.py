from re import M
from tkinter import Menu


class TodoDatabase:
    def __init__(self) -> None:
        self.todo_list = []


class TodoMenu():
    def __init__(self) -> None:
        todo_db = TodoDatabase()


if __name__ == "__main__":
    menu = TodoMenu()