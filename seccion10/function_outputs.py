# Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("carlos", "ALMADA") 
print(formated_string)


# El return dentro de una función hace que se termine la ejecución y lo que se declare debajo ya no va a ser ejecutado

def format_name_example(f_name, l_name):
    
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


print(format_name_example(input("Whats is your first name? "), input("What is your last name? ")))
    