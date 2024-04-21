# calculations.py


ELECTRICITY_EMISSION_FACTOR = 0.4  # Example: kgCO2e per kWh
WATER_USAGE_EMISSION_FACTOR = 0.298  # Example: kgCO2e per litre
CAR_TRAVEL_EMISSION_FACTOR = 0.404  # Example: kgCO2e per km
NON_RECYCLABLE_WASTE_EMISSION_FACTOR = 1.2  # Example: kgCO2e per kg
RECYCLABLE_WASTE_EMISSION_FACTOR = 0.8  # Example: kgCO2e per kg
FRUITS_VEG_EMISSION_FACTOR = 0.4  # Example: kgCO2e per kg

DIET_EMISSION_FACTORS = {
    'plant-based': 1.5,
    'vegetarian': 1.7,
    'high-meat': 3.3,
}

PUBLIC_TRANSPORT_EMISSION_FACTORS = {
    'bus': 0.105,
    'train': 0.041,
}

HEATING_TYPE_EMISSION_FACTORS = {
    'natural-gas': 0.2,
    'oil': 0.3,
    'electric': 0.8,
}

MEAT_EMISSION_FACTORS = {
    'beef': 27,
    'chicken': 6.9,
}

def calculate_individual_footprint(
    household_size,
    diet_type,
    car_travel_km,
    public_transport_mode,
    public_transport_distance,
    electricity_kwh,
    heating_type,
    heating_usage,
    non_recyclable_waste_kg,
    recyclable_waste_kg,
    water_usage_m3,
    meat_type,
    meat_dairy_eggs_kg,
    fruits_vegetables_kg,
):
    # Calculate the electricity emissions
    electricity_emissions = electricity_kwh * ELECTRICITY_EMISSION_FACTOR

    # Calculate the water emissions
    water_emissions = water_usage_m3 * 1000 * WATER_USAGE_EMISSION_FACTOR  # Convert m3 to liters

    # Calculate diet emissions
    diet_factor = DIET_EMISSION_FACTORS.get(diet_type, 0)
    diet_emissions = household_size * diet_factor * meat_dairy_eggs_kg

    # Calculate car travel emissions
    car_emissions = car_travel_km * CAR_TRAVEL_EMISSION_FACTOR

    # Calculate public transport emissions
    public_transport_factor = PUBLIC_TRANSPORT_EMISSION_FACTORS.get(public_transport_mode, 0)
    public_transport_emissions = public_transport_distance * public_transport_factor

    # Calculate heating emissions
    heating_factor = HEATING_TYPE_EMISSION_FACTORS.get(heating_type, 0)
    heating_emissions = heating_usage * heating_factor

    # Calculate emissions from waste
    non_recyclable_waste_emissions = non_recyclable_waste_kg * NON_RECYCLABLE_WASTE_EMISSION_FACTOR
    recyclable_waste_emissions = recyclable_waste_kg * RECYCLABLE_WASTE_EMISSION_FACTOR

    # Calculate emissions from food
    meat_factor = MEAT_EMISSION_FACTORS.get(meat_type, 0)
    meat_emissions = meat_dairy_eggs_kg * meat_factor
    fruits_vegetables_emissions = fruits_vegetables_kg * FRUITS_VEG_EMISSION_FACTOR

    # Calculate the total footprint
    total_footprint = (
        electricity_emissions +
        water_emissions +
        diet_emissions +
        car_emissions +
        public_transport_emissions +
        heating_emissions +
        non_recyclable_waste_emissions +
        recyclable_waste_emissions +
        meat_emissions +
        fruits_vegetables_emissions
    )

    return total_footprint 


def calculate_grade(total_footprint):
    if total_footprint < 6000:
        return "VERY LOW (Less than 600)"
    elif total_footprint < 16000:
        return "IDEAL (Less than 16000)"
    elif total_footprint < 22000:
        return "AVERAGE (Less than 22000)"
    else:
        return "TOO HIGH (More than 22000)"