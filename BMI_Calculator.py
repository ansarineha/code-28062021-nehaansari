import pandas as pd
import json
import csv


def calculate_bmi(weight, height):
	bmi = weight/(height*height)
	return bmi


with open("raw_data.json", "r") as json_file:
    json_data = json.load(json_file)

    bmi_list = []
    health_risk_list = []
    bmi_category_list = []

    for data in json_data:

        height = data['HeightCm']/100
        weight = data['WeightKg']
        bmi = calculate_bmi(height, weight)
  
        bmi_list.append(bmi)
        col_names = ['Gender', 'HeightCm', 'WeightKg']  

        with open('BMI_data.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=col_names)
            writer.writeheader()
            writer.writerows(json_data)
        file.close()


        if (bmi <= 18.4):
            bmi_category = bmi_category_list.append("Underweight")
            health_risk = health_risk_list.append(("Malnutrition risk"))

        elif ( bmi >= 18.5 and bmi <= 24.9):
            bmi_category = bmi_category_list.append("Normal Weight")
            health_risk = health_risk_list.append(("Low risk"))

        elif ( bmi >= 25 and bmi <= 29.9):
            bmi_category = bmi_category_list.append("Overweight")
            health_risk = health_risk_list.append(("Enhanced risk"))

        elif (  bmi >= 30 and bmi <= 34.9):
            bmi_category = bmi_category_list.append("Moderately Obese")
            health_risk_list.append(("Medium risk"))

        elif (  bmi >= 35 and bmi <= 39.9):
            bmi_category = bmi_category_list.append("Severely Obese")
            health_risk = health_risk_list.append(("High risk"))
        
        elif ( bmi >=40):
            bmi_category = bmi_category_list.append("Very Severely Obese")
            health_risk = health_risk_list.append(("Very High risk"))

        # print(health_risk_list)


    df = pd.read_csv("BMI_data.csv")
    df['BMI_value'] = bmi_list
    df['BMI_Category'] = bmi_category_list
    df['Health risk'] = health_risk_list

    df.to_csv('BMI_data.csv')

json_file.close()