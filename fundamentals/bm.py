print("Welcome to BodyMath: A smart BMI calculator")
print("This application is designed to assess Body-Mass-Index, a common metrix used for gauging body weight in relation to height\n")

print("\n1. Add patient\n2. Enter your details\n3. Display patient\n4. Medical advice\n5. Save and Exit")
choice = input("Enter your choice (1-5): ")

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def dietary_advise(category, blood_type, return_advice=False):
    category_lower = category.lower()
    advice = ""

    if category_lower == "underweight":
        if blood_type == "o":
            print("""You are advised to:
                    - Consult with a healthcare professional to identify potential underlying causes of low weight.
                    - Develop a balanced and nutrient-dense meal plan to support weight gain.
                    - Consider incorporating healthy fats, protein-rich foods, and a variety of fruits and vegetables into the diet.
                    - Collaborate with a registered dietitian to ensure nutritional needs are met.
                    - Rule out any medical conditions contributing to low weight.
                    - Focus on lean protein sources such as poultry, fish, and lean meats.
                    - Include whole grains like quinoa, brown rice, and oats.
                    - Incorporate healthy fats from sources like olive oil, avocados, and nuts.
                    """)
        elif blood_type == "a":
            print("""
            You are advised to:
                    - Consult with a healthcare professional to identify potential underlying causes of low weight.
                    - Develop a balanced and nutrient-dense meal plan to support weight gain.
                    - Collaborate with a registered dietitian to ensure nutritional needs are met.
                    - Rule out any medical conditions contributing to low weight. 
                    - Include lean protein sources such as fish, poultry, tofu, and legumes.
                    - Incorporate whole grains like quinoa, brown rice, and oats for energy.
                    - Include sources of healthy fats, such as avocados, nuts, and olive oil.
                    """)
        elif blood_type == "b":
            print("""
                You are advised to:
                - Consult with a healthcare professional to identify potential underlying causes of low weight.
                - Develop a balanced and nutrient-dense meal plan to support weight gain.
                - Consider incorporating protein-rich foods, and a variety of fruits and vegetables into the diet.
                - Collaborate with a registered dietitian to ensure nutritional needs are met.
                - Rule out any medical conditions contributing to low weight.
                - Incorporate lean protein sources like poultry, fish, and eggs.
                - Include whole grains such as brown rice and quinoa.
                - Consider dairy or fortified plant-based alternatives for additional nutrients.
                - Include sources of healthy fats like nuts, seeds, and olive oil.
                """)
        elif blood_type == "ab":
            print("""
                You are advised to
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Consider individual health goals and consult with a healthcare professional for personalized advice.
                - Maintain a balanced diet with a mix of protein, carbohydrates, and fats.
                - Focus on protein-rich foods like lean poultry, fish, and plant-based protein sources to support muscle development.
                - Incorporate sources of healthy fats such as avocados and olive oil for added calories.
                - Include a variety of colorful fruits and vegetables for a spectrum of nutrients.\""")
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "normal weight":You are advised to:
                    - Consult with a healthcare professional to identify potential underlying causes of low weight.
                    - Develop a balanced and nutrient-dense meal plan to support weight gain.
                    - Collaborate with a registered dietitian to ensure nutritional needs are met.
                    - Rule out any medical conditions contributing to low weight. 
                    - Include lean protein sources such as fish, poultry, tofu, and legumes.
                    - Incorporate whole grains like quinoa, brown rice, and oats for energy.
                    - Include sources of healthy fats, such as avocados, nuts, and olive oil.
                    """)
        elif blood_type == "b":
            print("""
                You are advised to:
                - Consult with a healthcare professional to identify potential underlying causes of low weight.
                - Develop a balanced and nutrient-dense meal plan to support weight gain.
                - Consider incorporating protein-rich foods, and a variety of fruits and vegetables into the diet.
                - Collaborate with a registered dietitian to ensure nutritional needs are met.
                - Rule out any medical conditions contributing to low weight.
                - Incorporate lean protein sources like poultry, fish, and eggs.
                - Include whole grains such as brown rice and quinoa.
                - Consider dairy or fortified plant-based alternatives for additional nutrients.
                - Include sources of healthy fats like nuts, seeds, and olive oil.
                """)
        elif blood_type == "ab":
            print("""
                You are advised to
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Consider individual health goals and consult with a healthcare professional for personalized advice.
                - Maintain a balanced diet with a mix of protein, carbohydrates, and fats.
                - Focus on protein-rich foods like lean poultry, fish, and plant-based protein sources to support muscle development.
                - Incorporate sources of healthy fats such as avocados and olive oil for added calories.
                - Include a variety of colorful fruits and vegetables for a spectrum of nutrients.""")
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "normal weight":
        if blood_type == "o":
            print("""
                You are advised to
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Consider individual health goals and consult with a healthcare professional for personalized advice.
                - Maintain a balanced diet with a mix of protein, carbohydrates, and fats.
                - Choose lean protein sources, including fish, poultry, beans, and lentils.
                - Prioritize a variety of colorful fruits and vegetables.""")
        elif blood_type == "a":
            print("""
                You are advised to
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Consider individual health goals and consult with a healthcare professional for personalized advice.
                - Maintain a balanced diet with a variety of fruits, vegetables, lean proteins, and whole grains.
                - Explore plant-based protein sources like beans, lentils, and tofu.
                - Minimize processed foods and focus on whole, nutrient-dense options.
                """)
        elif blood_type == "b":
            print("""
                You are advised to
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Consider individual health goals and consult with a healthcare professional for personalized advice.
                - Maintain a balanced diet with a mix of protein, carbohydrates, and fats.
                - Prioritize a variety of colorful vegetables for diverse nutrients.
                - Include moderate amounts of lean protein sources.
                - Choose whole, minimally processed foods over highly processed options.
                """)

        elif blood_type == "ab":
            print("""
                You are advised to
                - Maintain a balanced diet that includes a variety of food groups.
                - Focus on portion control and mindful eating to support overall health.
                - Engage in regular physical activity for cardiovascular health and overall well-being.
                - Schedule regular check-ups with a healthcare provider for preventive care.
                - Enjoy diverse protein sources including seafood, eggs, and legumes.                
                """)
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "overweight":
        if blood_type == "o":
            print("""
                You are advised to
                - Adopt a balanced and calorie-controlled diet with an emphasis on whole foods.
                - Engage in regular physical activity, incorporating both aerobic and strength-training exercises.
                - Consult with a registered dietitian for personalized dietary guidance.
                - Monitor portion sizes and practice mindful eating.
                - Discuss weight management goals with a healthcare provider for ongoing support.
                - Emphasize lean protein sources for satiety.
                - Minimize processed foods and focus on whole, nutrient-dense options.
                - Choose complex carbohydrates in moderation.
                """)
        elif blood_type == "a":
            print("""
            You are advised to
            - Adopt a balanced and calorie-controlled diet with an emphasis on whole foods.
            - Engage in regular physical activity, incorporating both aerobic and strength-training exercises.
            - Consult with a registered dietitian for personalized dietary guidance.
            - Discuss weight management goals with a healthcare provider for ongoing support.
            - Be mindful of portion sizes and practice moderation.
            - Consider incorporating more vegetarian meals with plant-based proteins.
            - Include regular physical activity in your routine.
            """)

        elif blood_type == "b":
            print("""
            You are advised to
            - Adopt a balanced and calorie-controlled diet with an emphasis on whole foods.
            - Engage in regular physical activity, incorporating both aerobic and strength-training exercises.
             - Consult with a registered dietitian for personalized dietary guidance.
            - Discuss weight management goals with a healthcare provider for ongoing support.
            - Be mindful of portion sizes and practice moderation.
            - Consider incorporating more vegetarian meals with plant-based proteins.
            - Include regular physical activity in your routine.
            """)

        elif blood_type == "b":
            print("""
            You are advised to
            - Adopt a balanced and calorie-controlled diet with an emphasis on whole foods.
            - Engage in regular physical activity, incorporating both aerobic and strength-training exercises.
            - Consult with a registered dietitian for personalized dietary guidance.
            - Monitor portion sizes and practice mindful eating.
            - Discuss weight management goals with a healthcare provider for ongoing support.
            - Choose complex carbohydrates in moderation.
            - Emphasize lean protein sources for satiety.
            - Minimize the intake of sugary snacks and beverages.
            """)

        elif blood_type == "ab":
            print("""
            You are advised to
            - Adopt a balanced and calorie-controlled diet with an emphasis on whole foods.
            - Engage in regular physical activity, incorporating both aerobic and strength-training exercises.
            - Consult with a registered dietitian for personalized dietary guidance.
            - Monitor portion sizes and practice mindful eating.
            - Choose lean protein options to support weight management.
            - Opt for fiber-rich foods like whole grains, legumes, and vegetables for satiety.
            - Stay well-hydrated with water and herbal teas to support metabolism.
            """)
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "obese":
        if blood_type == "o":
            print("""
                You are advised to
                - Seek guidance from healthcare professionals for a comprehensive weight management plan.
                - Adopt a balanced and calorie-controlled diet, emphasizing whole foods.
                - Incorporate regular physical activity into daily routines, with a mix of aerobic and strength-training exercises.
                - Consider behavioral counseling or support groups for weight management.
                - Discuss potential medical interventions, such as medications or bariatric surgery, if appropriate.
                """)

        elif blood_type == "a":
            print("""
                You are advised to
                - Seek guidance from healthcare professionals for a comprehensive weight management plan.
                - Adopt a balanced and calorie-controlled diet, emphasizing whole foods.
                - Incorporate regular physical activity into daily routines, with a mix of aerobic and strength-training exercises.
                - Consider behavioral counseling or support groups for weight management.
                - Discuss potential medical interventions, such as medications or bariatric surgery, if appropriate.
                """)

        elif blood_type == "b":
            print(""" 
            You are advised to
                - Seek guidance from healthcare professionals for a comprehensive weight management plan.
                - Adopt a balanced and calorie-controlled diet, emphasizing whole foods.
                - Incorporate regular physical activity into daily routines, with a mix of aerobic and strength-training exercises.
                - Consider behavioral counseling or support groups for weight management.
                - Discuss potential medical interventions, such as medications or bariatric surgery, if appropriate.
                - Pay attention to portion sizes to manage calorie intake.
                """)
        elif blood_type == "ab":
            print("""
                You are advised to
                - Seek guidance from healthcare professionals for a comprehensive weight management plan.
                - Adopt a balanced and calorie-controlled diet.
                - Incorporate regular aerobic and strength-training exercises.
                - Prioritize whole, unprocessed foods for nutritional density.
                - Incorporate regular physical activity tailored to individual abilities and preferences.
            """)
        else:
            print("Invalid blood type for the given category")
    else:
        print("Invalid category")

        return advice if return_advice else ""

class Patient:
    def __init__(self, name, gender, blood_type, age):
            self.name = name
            self.gender = gender
            self.blood_type = blood_type
            self.age = age

    def display_patient_info(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nBlood Type: {self.blood_type}\nAge: {self.age}")

    def save_to_file(self, bmi, category, advice):
        file_name = f"{self.name}_health_report.txt"
        with open(file_name, "w") as file:
            file.write(f"Name: {self.name}\nGender: {self.gender}\nBlood Type: {self.blood_type}\nAge: {self.age}\n")
            file.write(f"BMI: {bmi:.2f}\nCategory: {category}\n")
            file.write("Medical Advice:\n")
            file.write(advice or "")

    def run_application(self):
        category = ""
        weight = 0.0
        height = 0.0
        bmi = 0.0
        advice = ""

    while True:
        print("\n1. Add patient\n2. Enter your details\n3. Display patient\n4. Medical advice\n5. Save and Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            self.name = input("Enter your name: ")
            self.gender = input("Enter your gender: ")
            self.blood_type = input("Enter your blood type (O, A, B, AB): ").lower()
            self.age = input("Enter your age: ")
        elif choice == "2":
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))
            category = bmi_calculator(weight, height)
            print(f"Your BMI is {bmi:.2f}, and your category is {category}")
        elif choice == "3":
            self.display_patient_info()
        elif choice == "4":
            advice = dietary_advise(category, self.blood_type, return_advice=True)
            print(advice)
        elif choice == "5":
            self.save_to_file(bmi, category, advice)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


patient = Patient()
patient.run_application()
                                                                                     