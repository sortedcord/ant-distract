from cursesmenu import CursesMenu

def menugen(option_list, title="option"):
    option_list.insert(0, f"Add new {title}")

    print(option_list)

    while True:
        selection = CursesMenu.get_selection(option_list)

        if selection == 0:
            new_option = input(f"Enter new {title}: ")
            option_list.insert(1,new_option)
            continue
        else:
            break
    return option_list[selection], option_list[1:]
