#!/usr/bin/env python3
# pip install console-menu
# https://github.com/aegirhall/console-menu

import time
from consolemenu import *
from consolemenu.items import *


def continue1():
  time.sleep(1)
  x = input("Press any key to continue.")


def test():
  print("[ test ]")
  continue1()


def test3():
  print("[ test3 ]")
  continue1()


menu = ConsoleMenu("Title: Simple test", "Subtitle: Python console-menu")

# --- items ---
# MenuItem is the base class for all items, it doesn't do anything when selected
## menu_item = MenuItem("-------")

# A FunctionItem runs a Python function when selected

function_item1 = FunctionItem("Call a test python function", test)
function_item2 = FunctionItem("Call a input Python function", input, ["Enter an input: "])
function_item3 = FunctionItem("Call a test3 python function", test3)

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# ----------------------------
## menu.append_item(menu_item)
menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(command_item)
menu.append_item(submenu_item)

menu.show()
