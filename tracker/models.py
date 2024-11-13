from django.db import models
from django.contrib.auth.models import User
from .calculations import calculate_individual_footprint, calculate_grade


class CarbonFootprintRecord(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_recorded = models.DateTimeField(auto_now_add=True)
    household_size = models.IntegerField()

    # Travel
    car_travel_km = models.FloatField()
    public_transport_mode = models.CharField(max_length=50, choices=[
        ('bus', 'Bus'),
        ('train', 'Train'),
    ])
    public_transport_distance = models.FloatField()

    # Energy consumption
    electricity_kwh = models.FloatField()
    heating_type = models.CharField(max_length=50, choices=[
        ('natural-gas', 'Natural Gas'),
        ('oil', 'Oil'),
        ('electric', 'Electric'),
    ])
    heating_usage = models.FloatField()

    # Waste
    non_recyclable_waste_kg = models.FloatField()
    recyclable_waste_kg = models.FloatField()

    # Water
    water_usage_m3 = models.FloatField()

    # Diet
    diet_type = models.CharField(max_length=50, choices=[
        ('plant-based', 'Plant-based'),
        ('vegetarian', 'Vegetarian'),
        ('high-meat', 'High-meat'),
    ])
    meat_type = models.CharField(max_length=50, choices=[
        ('beef', 'Beef'),
        ('chicken', 'Chicken'),
    ], null=True, blank=True)  # Nullable as it might not apply to plant-based diets
    meat_dairy_eggs_kg = models.FloatField()
    fruits_vegetables_kg = models.FloatField()

    # Calculated footprint
    total_footprint = models.FloatField(editable=False, null=True, blank=True)  # Not editable because it's set programmatically
    grade = models.CharField(editable=False, null=True, max_length=50)

    def save(self, *args, **kwargs):
        # Call the calculate_individual_footprint function here to calculate the total_footprint
        # before saving the model instance. You might need to import the function.
        self.total_footprint = calculate_individual_footprint(
            household_size=self.household_size,
            diet_type=self.diet_type,
            car_travel_km=self.car_travel_km,
            public_transport_mode=self.public_transport_mode,
            public_transport_distance=self.public_transport_distance,
            electricity_kwh=self.electricity_kwh,
            heating_type=self.heating_type,
            heating_usage=self.heating_usage,
            non_recyclable_waste_kg=self.non_recyclable_waste_kg,
            recyclable_waste_kg=self.recyclable_waste_kg,
            water_usage_m3=self.water_usage_m3,
            meat_type=self.meat_type,
            meat_dairy_eggs_kg=self.meat_dairy_eggs_kg,
            fruits_vegetables_kg=self.fruits_vegetables_kg,
        )

        self.grade = calculate_grade(self.total_footprint)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"Carbon Footprint Record for {self.user.username} on {self.date_recorded.strftime('%Y-%m-%d')} and total footprint of {self.total_footprint}"
    
    class Meta:
        ordering = ['-date_recorded']