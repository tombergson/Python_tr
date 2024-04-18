def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours": 
        return f"{num_of_days} days are {num_of_days * 24} hours"

    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsuported unit" 

def validate_and_execute(days_and_unit_dictionary):
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calc_values = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calc_values)
        elif user_input_number == 0:
            print("Wpisałeś zero! Popraw!")
        else:
            print("Wpisałeś ujemną liczbę! Popraw!")

    except ValueError:
            print("Nie wpisałeś liczby!")  


user_input_message = "Wpisz liczbę dni oraz jednostkę:\n"
   
