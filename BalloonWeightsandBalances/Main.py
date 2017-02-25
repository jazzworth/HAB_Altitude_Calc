import Atmosphere
import Aircraft
import Calculate


pressure1 = Atmosphere.Pressure_Altitude()
balloon1 = Aircraft.Balloon()

balloon1.determine_the_units()

balloon1.enter_the_volume()

balloon1.convert_cubic_feet_to_cubic_meters()

balloon1.enter_system_weight()

balloon1.convert_system_weight_lbs_to_kg()

balloon1.enter_the_max_temp()

balloon1.convert_temp_to_kelvin()

pressure1.enter_max_altitude()

pressure1.calculate_pressure_at_altitude()

pressure1.enter_launch_temp()

pressure1.convert_launch_temp_to_kelvin()

calc_lift = Calculate.CalculateLift()

calc_lift.calculate_lift()

calc_lift.convert_kg_lbs()


