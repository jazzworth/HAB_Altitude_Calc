import Aircraft



class Pressure_Altitude:
    #constants used to calculate the air pressure at altitude
    STANDARD_PRESSURE_Po = 101325 #in Pa
    STANDARD_TEMP_To = 288.15 #in K
    EARTH_SURFACE_GRAVITATIONAL_ACCELERATION_g = 9.80665 #in m/s2
    TEMPERATURE_LAPSE_RATE_L = 0.0065 #in K/m
    UNIVERSAL_GAS_CONSTANT_R = 8.31447 #IN j/(mol-k)
    MOLAR_MASS_OF_DRY_AIR_M = 0.0289644 #in kg/mol
    EXPONENT = (EARTH_SURFACE_GRAVITATIONAL_ACCELERATION_g * MOLAR_MASS_OF_DRY_AIR_M) / (UNIVERSAL_GAS_CONSTANT_R * TEMPERATURE_LAPSE_RATE_L)
    max_altitude = 0
    pressure_at_altitude = 0
    launch_temp = 0

    def __init__(self):
        pass

    def enter_max_altitude(self):
        while True:
            try:
                if Aircraft._unit == 'I':
                    Pressure_Altitude.max_altitude = float(input("Please enter the maximum altitude in feet MSL:\n"))
                    Pressure_Altitude.max_altitude *= 0.3048
                    break
                else:
                    Pressure_Altitude.max_altitude = float(input("Please enter the maximum altitude in meters MSL:\n"))
                    return Pressure_Altitude.max_altitude
                    break
            except ValueError:
                print("\nPlease only use numbers!\n")

    def calculate_pressure_at_altitude(self):
        Pressure_Altitude.pressure_at_altitude =\
            Pressure_Altitude.STANDARD_PRESSURE_Po * (1 - (Pressure_Altitude.TEMPERATURE_LAPSE_RATE_L *
                                                                                   Pressure_Altitude.max_altitude) / Pressure_Altitude.STANDARD_TEMP_To) ** Pressure_Altitude.EXPONENT
        Pressure_Altitude.pressure_at_altitude /= 100
        return Pressure_Altitude.pressure_at_altitude

    def enter_launch_temp(self):
        while True:
            try:
                if Aircraft._unit == 'I':
                    Pressure_Altitude.launch_temp = float(input("Please enter the expected temperature @ Altitude in Fahrenheit: \n"))
                    return Pressure_Altitude.launch_temp
                    break
                else:
                    Pressure_Altitude.launch_temp = float(input("Please enter the expected temperature @ Altitude in Celsius: \n"))
                    return Pressure_Altitude.launch_temp
                    break
            except ValueError:
                print("\nPlease use numbers only")

    def convert_launch_temp_to_kelvin(self): #K = 5/9 (° F - 32) + 273 and K = ° C + 273
        if Aircraft._unit == 'I':
            Pressure_Altitude.launch_temp = (Pressure_Altitude.launch_temp + 459.67) * (5/9)
        else:
            Pressure_Altitude.launch_temp += 273.15
            return Pressure_Altitude.launch_temp

    def convert_launch_temp_lapse_rate(self):
        Pressure_Altitude.launch_temp += Pressure_Altitude.launch_temp - Pressure_Altitude.STANDARD_TEMP_To - Pressure_Altitude.TEMPERATURE_LAPSE_RATE_L * Pressure_Altitude.max_altitude
        return Pressure_Altitude.launch_temp

