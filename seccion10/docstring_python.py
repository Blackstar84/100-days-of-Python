"""
Esto es un docstring, no se recomienda utilizarlo como un comentario, para eso utilizar los # 
en multilínea, no utilizar el docstring como comentarios
"""
formatted_name = "Carlos"

length = len(formatted_name)

print(length)

# Lo que se encuentra dentro de la función aparecerá como explicación
# cuando llamemos a nuestra función
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name("carlos", "almada"))

