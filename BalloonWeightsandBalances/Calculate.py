import Aircraft
import Atmosphere


class CalculateLift(Aircraft.Balloon, Atmosphere.Pressure_Altitude):
    lift_in_kg = 0

    def calculate_lift(self):

        CalculateLift.lift_in_kg = Aircraft.Balloon.envelope_volume * (Atmosphere.Pressure_Altitude.pressure_at_altitude / 2.87) * (
            (1 / Atmosphere.Pressure_Altitude.launch_temp) - (1 / Aircraft.Balloon.max_envelope_temp))
        return CalculateLift.lift_in_kg

    def convert_kg_lbs(self):
        if Aircraft._unit == 'I':
            CalculateLift.lift_in_kg = (CalculateLift.lift_in_kg *2.20462) - (Aircraft.Balloon.system_weight * 2.20462)
            print("Your total lift after system weight is:  ",  round(CalculateLift.lift_in_kg,2) , "lbs\n")
        else:
            CalculateLift.lift_in_kg -= Aircraft.Balloon.system_weight
            print("Your total lift after system weight is: ",  round(CalculateLift.lift_in_kg) , "kgs\n")
        return CalculateLift.lift_in_kg