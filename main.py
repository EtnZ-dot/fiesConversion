# EtnZ

import gui
import fies
import about


def menu():
    gui.window("°Fies Conversion", 0, "center")
    gui.window("[1] Convert from °Fies to °Celsius", 2)
    gui.window("[2] Convert from °Celsius to °Fies", 2)
    gui.window("[3] About", 2)
    gui.window("[4] Quit", 1)
    user_input = gui.choice(4)

    if user_input == 1:
        gui.window("Please input your desired °Fies to convert into °Celsius", 0, "center")
        num_input = gui.is_it_a_number()
        num_ans = fies.fies_to_celsius(num_input)
        ans = str(str(num_input) + "°Fies = " + str(num_ans) + "°Celsius")
        gui.window(ans)
        gui.window("Press enter to return back to menu.", 1)
        input("> ")

    elif user_input == 2:
        gui.window("Please input your desired °Celsius to convert into °Fies", 0, "center")
        num_input = gui.is_it_a_number()
        num_ans = fies.celsius_to_fies(num_input)
        ans = str(str(num_input) + "°Celsius = " + str(num_ans) + "°Fies")
        gui.window(ans)
        gui.window("Press enter to return back to menu.", 1)
        input("> ")

    elif user_input == 3:
        about.menu()

    elif user_input == 4:
        quit()

    menu()


menu()
