_unit = ''  # singleton pattern


class Balloon:
    envelope_volume = 0
    max_payload = 0
    max_envelope_temp = 0
    system_weight = 0

    def __init__(self):
        pass

    def convert_cubic_feet_to_cubic_meters(self):
        if _unit == 'I':
            Balloon.envelope_volume *= 0.0283168
        else:
            return Balloon.envelope_volume

    def determine_the_units(self):
        prompt_user_on = True
        global _unit
        while prompt_user_on:
            _unit = str(input("for Imperial measurements (eg inHg, cubic feet, Fahrenheit), please enter 'I':\n"
                              "for Metric measurements (eg hPa, cubic meters, Celsius), please"
                              "enter 'M': \n")).upper()
            if _unit != 'I' and _unit != 'M':
                print("Please enter 'I' or 'M': \n")
            else:
                prompt_user_on = False
                return _unit

    def enter_the_volume(self):
        while True:
            try:
                if _unit == 'I':
                    Balloon.envelope_volume = int(input("Let's enter information "
                                                     "about your balloon.\n\n"
                                                     "Please enter the envelope volume in cubic feet: \n"))
                    return Balloon.envelope_volume
                    break
                else:
                    Balloon.envelope_volume = int(input("Let's enter information "
                                                     "about your balloon.\n\n"
                                                     "Please enter the envelope volume in cubic meters: \n"))
                    return Balloon.envelope_volume
                    break
            except ValueError:
                print("\nPlease only use numbers!\n")

    def enter_the_max_system_payload(self):
        while True:
            try:
                if _unit == 'I':
                    Balloon.max_payload = float(input("Please enter the maximum system payload in lbs:\n"))
                    return Balloon.max_payload
                    break
                else:
                    Balloon.max_payload = float(input("Please enter the maximum system payload in kg:\n"))
                    return Balloon.max_payload
                    break
            except ValueError:
                print("\nPlease only use numbers!\n")

    def convert_payload_lbs_to_kg(self):
        if _unit == 'I':
            Balloon.max_payload *= 0.453592
        else:
            return Balloon.max_payload

    def enter_the_max_temp(self):
        while True:
            try:
                if _unit == 'I':
                    Balloon.max_envelope_temp = float(
                        input("Please enter the maximum envelope temperature in Fahrenheit: \n"))
                    return Balloon.max_envelope_temp
                    break
                else:
                    Balloon.max_envelope_temp = float(
                        input("Please enter the maximum envelope temperature in Celsius: \n"))
                    return Balloon.max_envelope_temp
                    break
            except ValueError:
                print("\nPlease use numbers only")

    def convert_temp_to_kelvin(self):  # K = 5/9 (° F - 32) + 273 and K = ° C + 273
        if _unit == 'I':
            Balloon.max_envelope_temp = (Balloon.max_envelope_temp + 459.67) * (5/9)
        else:
            Balloon.max_envelope_temp += 273.15
            return Balloon.max_envelope_temp

    def enter_system_weight(self):
        while True:
            try:
                if _unit == 'I':
                    Balloon.system_weight = float(input("Please enter the system weight in lbs.  This usually"
                                                     "includes the weight of the envelop, burner, basket"
                                                     ", and 2 tanks: \n"))
                    return Balloon.system_weight
                    break
                else:
                    Balloon.system_weight = float(input("Please enter the system weight in kg.  This usually"
                                                     "includes the weight of the envelop, burner, basket"
                                                     ", and 2 tanks: \n"))
                    return Balloon.system_weight
                    break
            except ValueError:
                print("\nPlease use numbers only")

    def convert_system_weight_lbs_to_kg(self):
        if _unit == 'I':
            Balloon.system_weight *= 0.453592
        else:
            return Balloon.system_weight
