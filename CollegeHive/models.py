from django.db import models

# Create your models here.
class Listing(models.Model):
    Title=models.CharField(max_length=255)
    Image_Path=models.CharField(max_length=255)
    Price_Rs=models.CharField(max_length=20)
    Status=models.CharField(max_length=50)          # Values : For Rent, Occupied
    Owner_Name=models.CharField(max_length=100)
    No_Bathrooms=models.IntegerField()
    No_Bedrooms=models.IntegerField()
    Map_Location=models.CharField(max_length=255)
    Agent_Email=models.CharField(max_length=255)
    Property_Type=models.CharField(max_length=100)
    Agent_Phone=models.BigIntegerField()
    Size_sqft=models.IntegerField()
    Vacant_Rooms=models.IntegerField()
    No_Floors=models.IntegerField()

    def __str__(self):
        return self.Title

