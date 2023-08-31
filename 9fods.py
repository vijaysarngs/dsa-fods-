import pandas as pd
property_data1={
    "propert_ID":[23,21,20,78],
    "location":["chennai","chennai","trichy","madurai"],
    "number_of_bedrooms":[3,4,5,6],
    "sq_ft":[210,220,432,980],
    "listing_price":[21000,32000,32111,98000]
}
property_data=pd.DataFrame(property_data1)
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
print(average_price_per_location)

properties_more_than_4_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_4_bedrooms = len(properties_more_than_4_bedrooms)
print("Number of properties with more than four bedrooms:", num_properties_more_than_4_bedrooms)

property_with_largest_area = property_data[property_data["sq_ft"] == property_data["sq_ft"].max()]
print("Property with the largest area:")
print(property_with_largest_area)
