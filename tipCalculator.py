print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))

#bill_with_tip = tip / 100 * bill + bill

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Para dar formato a los números utilizamos {:.2f}.format(variable a Convertir)
# Esto pondra dos decimales luego del punto a los números flotantes
# Ejemplo: si utilizamos los valores proveídos 150 el valor de la cuenta, 12 tips 5 personas
# esto debería dar 33.60, si utilizamos round en lugar de esto, nos devolverá 33.6 faltandole
# así el cero luego del 6, debería ser 33.60 el monto final que debe pagar cada uno.
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")


