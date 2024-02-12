# Mi solución

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
# Mi versión

def days_in_month(year, month):
    # Acordarse que la lista empieza en cero 0
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    year_leap_or_not = is_leap(year)

    # Por ese motivo si es leap year el mes de febrero debe tener 29 días
    # Para modificarlo lo ubicamos en la posición 1 de nuestra lista que correspondería
    # a Febrero
    if month == 2 and year_leap_or_not == True:
        month_days[1] = 29

    print(year_leap_or_not)    
    # Retornamos la cantidad de días que hay en el mes que indicó el usuario
    # Como iniciamos en 0 debemos restarle 1 al proveído por el usuario
    # para asi dar con el mes solicitado ya que la lista inicia en 0
    # siendo 0 el primer mes de Enero, entonces si el usuario en mes pasa 1
    # debemos restarle 1 a ese mes para poder obtener el mes de Enero.
    return month_days[month-1] 

# Version Clase
def days_in_month(year, month):
    # Acordarse que la lista empieza en cero 0
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    year_leap_or_not = is_leap(year)

    # Por ese motivo si es leap year el mes de febrero debe tener 29 días
    # Para modificarlo lo ubicamos en la posición 1 de nuestra lista que correspondería
    # a Febrero
    if month == 2 and year_leap_or_not == True:
        return 29
    else:
       return month_days[month-1]
    
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
