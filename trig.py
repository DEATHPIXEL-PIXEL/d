import math

def calculate_trig_functions():
    angle = float(input("Enter the angle in degrees: "))
    radians = math.radians(angle)

    
    sin_value = math.sin(radians)
    cos_value = math.cos(radians)
    tan_value = math.tan(radians)
    csc_value = 1 / sin_value
    sec_value = 1 / cos_value
    cot_value = 1 / tan_value
    
    print("\nResults for", angle, "°:")
    print("sin =", round(sin_value, 6))
    print("cos =", round(cos_value, 6))
    print("tan =", round(tan_value, 6))
    print("csc =", round(csc_value, 6))
    print("sec =", round(sec_value, 6))
    print("cot =", round(cot_value, 6))

if __name__ == "__main__":
    calculate_trig_functions()
