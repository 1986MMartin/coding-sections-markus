
def function_01():
    print("Function 1")
    print("---------------")

def function_02():
    print("Function 2")
    print("---------------")

def function_03():
    print("Function 3")
    print("---------------")


select_options = {
        "F1": function_01,
        "F2": function_02,
        "F3": function_03
        }

for sel in select_options:
    sel_function = select_options[sel]
    sel_function()

