from pybricks.tools import hub_menu

selected = hub_menu("1", "2", "3", "4", "5", "B", "6")

if selected == "1":
    import run1
elif selected == "2":
    import run2
elif selected == "3":
    import run3
elif selected == "4":
    import run4
elif selected == "5":
    import run5
elif selected == "B":
    import run5_in_case_there_is_no_time
elif selected == "6":
    import run6
