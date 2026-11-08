# Project1:
# phase 1 : développement d'un moteur de calcul
# creation read_float function:
def read_float(message, minimum=None, maximum=None):# message is varriable to write an message 
    while True:  # minimum ,maximum doesn't have a values now 
        try:
            value = float(input(message))
        except ValueError:
            print("Valeur invalide : entre un nombre.")
            continue
        if minimum is not None and value < minimum:
            print(f"La valeur doit être ≥ {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"La valeur doit être ≤ {maximum}.")
            continue
        return value

# creation Enter_Data function:
def Enter_Data():
    voltage = read_float("Enter the voltage value (V): ", minimum=0)
    current = read_float("Enter the current value (A): ", minimum=0)
    power_factor = read_float("Enter the power factor (0 to 1): ", minimum=0, maximum=1)
    time_h = read_float("Enter the duration (hours): ", minimum=0)
    return voltage, current, power_factor, time_h

 # creation motor_calculator function:
def motor_calculator(voltage, current, power_factor, time_h):
    power = voltage * current * power_factor   # P = U × I × cos(φ), en W
    energy = power * time_h                    # E = P × t, en Wh
    return power, energy
# Programme principal
voltage, current, power_factor, time_h = Enter_Data()
power, energy = motor_calculator(voltage, current, power_factor, time_h)

print(f"The power value: {power} W")
print(f"The energy value: {energy} Wh")
