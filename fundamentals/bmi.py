#!/usr/bin/python3
import time
import os
import MySQLdb

print()
print("Welcome to BodyMath: A smart BMI calculator")
time.sleep(3)
print()
print("The all-in-one health and wellness app designed to empower individuals on their weight management journey.") 
time.sleep(1)
print("This innovative app seamlessly combines BMI tracking with personalized insights based on blood type,")
time.sleep(1)
print("creating a holistic approach to achieving and maintaining a healthy weight.")
time.sleep(1)

class Patient:
    def __init__(self, name="", gender="", blood_type="", age=""):
        self.name = name
        self.gender = gender
        self.blood_type = blood_type
        self.age = age

    def display_patient_info(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nBlood Type: {self.blood_type}\nAge: {self.age}")

    def save_to_file(self, bmi, category, advice):
        os.makedirs("health_reports", exist_ok=True)
        file_name = f"{self.name}_health_report.txt"
        file_path = os.path.join("health_reports", file_name)
        with open(file_path, "w") as file:
            file.write(f"Name: {self.name}\nGender: {self.gender}\nBlood Type: {self.blood_type}\nAge: {self.age}\n")
            file.write(f"BMI: {bmi:.2f}\nCategory: {category}\n")
            file.write("Medical Advice:\n")
            file.write(advice or "")
           
    def save_to_database(self, file_name):
            # Establish a connection to MySQL
            connection = MySQLdb.connect(
                host="localhost",
                user="root",
                password="2406",
                port="3306"
            )

            # Create a cursor object
            cursor = connection.cursor()

            # Create the 'bodymath' database if it doesn't exist
            create_database_query = "CREATE DATABASE IF NOT EXISTS bodymaths;"
            cursor.execute(create_database_query)

            # Use the 'bodymath' database
            cursor.execute("USE bodymaths;")

            # Create the 'Patient' table if it doesn't exist
            create_patient_table_query = (
                "CREATE TABLE IF NOT EXISTS Patient ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "name VARCHAR(255) NOT NULL,"
                "gender VARCHAR(10) NOT NULL,"
                "blood_type VARCHAR(5) NOT NULL,"
                "age INT NOT NULL"
                ");"
            )
            cursor.execute(create_patient_table_query)

            # Create the 'report' table if it doesn't exist
            create_report_table_query = (
                "CREATE TABLE IF NOT EXISTS report ("
                "id INT AUTO_INCREMENT PRIMARY KEY,"
                "name VARCHAR(255) NOT NULL,"
                "gender VARCHAR(10) NOT NULL,"
                "blood_type VARCHAR(5) NOT NULL,"
                "age INT NOT NULL,"
                "patient_reports TEXT NOT NULL"
                ");"
            )
            cursor.execute(create_report_table_query)

            # Read content from the file
            with open(file_name, "r") as file:
                file_content = file.read()

            # Insert data into the 'report' table
            insert_data_query = (
                "INSERT INTO report (name, gender, blood_type, age, patient_reports) VALUES (%s, %s, %s, %s, %s);"
            )
            data = (self.name, self.gender, self.blood_type, int(self.age), file_content)
            cursor.execute(insert_data_query, data)

            # Commit changes and close the connection
            connection.commit()

            cursor.close()
            connection.close()

    def run_application(self):
        category = ""
        weight = 0.0
        height = 0.0
        bmi = 0.0
        advice = ""
        diet=""
        sports=""
        doctor=""
    
        while True:
            print("\n1. Add patient\n2. Enter your details for BMI calculation\n3. Display patient information\n4. Medical advice\n5. Dietary advice\n6. Access your exercise routine\n7. Meet professional personnels and nutritionists\n8. Save and Exit")
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.name = input("Enter your name: ")
                self.gender = input("Enter your gender: ")
                self.blood_type = input("Enter your blood type (O, A, B, AB): ").lower()
                self.age = input("Enter your age: ")
            elif choice == "2":
                try:
                    weight = float(input("Enter your weight (kg): "))
                    height = float(input("Enter your height (m): "))
                    bmi, category = bmi_calculator(weight, height)
                    print(f"Your BMI is {bmi:.2f}, and your category is {category}")
                except ValueError:
                    print("Invalid input! Please enter numeric values for weight and height! ")

            elif choice == "3":
                self.display_patient_info()
                time.sleep(10)
            elif choice == "4":
                advice = medical_advise(category, self.blood_type, return_advice=True)
                print(advice)
                time.sleep(30)
            elif choice == "5":
                diet = dietary_advice(category, self.blood_type, return_diet=True)
                print(diet)
            elif choice == "6":
                sports = exercises(category, return_sports=True)
                print(sports)
            elif choice == "7":
                print("""
                It is always better to seek advice from professionals.
                Here is a list of recommended professionals like doctors and nutritionits.
                Nutritionists:
                - Nutrition Cabinet: LA PERVENCHE NUTRITION CABINET
                  tel: 0780 626 378
                  location: Opposite to, KK 10 Ave, Kigali
                - Nutrition Cabinet: NUTRI-SANTE LTD
                  tel: 0788 729 794
                  location: Opposite to, KK 10 Ave, Kigali
                - Nutri-Mediplus Nutrition cabinet
                  tel: 0788 940 474
                  location: KG 165 St, 2A, Kigali
                - Amazon Nutrition Cabinet
                  tel: 0788 906 119
                  location: KG 173 St, Kigali
                - NutriFirst Ltd
                  tel: 0793 605 108
                  location: KK 222 St, Kigali
                
                Hospitals:
                
                - CHUK
                    tel: 0788 304 005
                    location: KN 4 Ave, Kigali
                - KIBAGABAGA HOSPITAL
                    tel:0788 732 945
                    location:KG 19 Ave, Kigali	
                - La Croix du Sud Hospital
                    tel: 0785 246 882
                    location: KG 201 St, Kigali
                - KANOMBE MILITARY HOSPITAL	
                    location: 25C9+H57, Kigali
                    info@rwandamilitaryhospital.rw
                - KING FAISAL HOSPITAL	
                    tel: 0788 123 200
                    info@kfh.rw 
                  
                """)
            elif choice == "8":
                self.save_to_file(bmi, category, advice)
                if 'file_name' in locals():
                    self.save_to_database(file_name)
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

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



def dietary_advice(category, blood_type, return_diet=False):
    category_lower = category.lower()
    diet=""

    if category_lower == "underweight":
        if blood_type == "o" or blood_type == "O":
            diet = """ Dietary advice :
            overall idea:
            - Focus on lean proteins like meat, poultry, and fish.
            - Include vegetables and fruits, with an emphasis on green leafy vegetables.
            - Consider snacks with nuts or seeds.

            meal plan:
            Monday:
                Breakfast:
                    Scrambled eggs with spinach and whole-grain toast.
                Lunch:
                    Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                    Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                    Greek yogurt with sliced berries and a handful of almonds.
                Lunch:
                    Lentil soup with a side of whole-grain bread.
                Dinner:
                    Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                    Smoothie with banana, spinach, and almond milk.
                Lunch:
                    Turkey and avocado wrap with whole wheat tortilla.
                Dinner:
                    Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                    Whole grain toast with avocado and poached eggs.
                Lunch:
                    Quinoa bowl with mixed vegetables and grilled chicken.
                Dinner:
                    Grilled salmon with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                    Oatmeal with sliced almonds and mixed berries.
                Lunch:
                    Chickpea salad with feta cheese and olive oil dressing.
                Dinner:
                    Baked cod with sweet potato wedges.
            Saturday:
                Breakfast:
                    Chia seed pudding with almond milk and topped with mixed berries.
                Lunch:
                    pinach and tomato omelette with whole-grain toast.
                Dinner:
                    Stir-fried beef with broccoli and brown rice.
            Sunday:
                Breakfast:
                    Cottage cheese with pineapple.
                Lunch:
                    Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                    Grilled chicken with quinoa and steamed asparagus.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.   
            """
        elif blood_type == "a" or blood_type == "A":
            diet = """ Dietary addice:
            general idea:
            - Emphasize plant-based proteins like beans and tofu.
            - Include whole grains like quinoa and brown rice.
            - Opt for smaller, more frequent meals.
            meal plan:
            Monday:
                Breakfast:
                    Oatmeal with sliced banana and almond butter.
                Lunch:
                    Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                    Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                    Fruit smoothie with spinach, berries, and soy milk.
                Lunch:
                    Lentil soup with a side of whole-grain bread.
                Dinner:
                    Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                    Whole grain toast with avocado and poached eggs.
                Lunch:
                    Chickpea and vegetable curry with basmati rice.
                Dinner:
                    Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                    Greek yogurt with honey and mixed berries.
                Lunch:
                    Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                    Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                    Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                    Spinach and feta omelette with whole-grain toast.
                Dinner:
                    Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                    Smoothie with pineapple, kale, and coconut water.
                Lunch:
                    Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                    Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                    Cottage cheese with sliced peaches.
                Lunch:
                    Mixed greens salad with grilled salmon.
                Dinner:
                    Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.         
            """    
        elif blood_type == "b" or blood_type == "B":
            diet = """ Dietary addice:
            general idea:
          

            meal plan:
            Monday:
                Breakfast:
                    Scrambled eggs with spinach and whole-grain toast.
                Lunch:
                    Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                    Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                    Fruit smoothie with berries, banana, and almond milk.
                Lunch:
                    Lentil soup with a side of whole-grain bread.
                Dinner:
                    Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                    Whole grain toast with avocado and poached eggs.
                Lunch:
                    Chickpea and vegetable curry with basmati rice.
                Dinner:
                    Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                    Greek yogurt with honey and mixed berries.
                Lunch:
                    Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                    Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                    Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                    Spinach and feta omelette with whole-grain toast.
                Dinner:
                    Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                    Smoothie with pineapple, kale, and coconut water.
                Lunch:
                    Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                    Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                    Cottage cheese with sliced peaches.
                Lunch:
                    Mixed greens salad with grilled salmon.
                Dinner:
                    Stir-fried tofu with soba noodles and broccoli.
            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
           """
        elif blood_type == "ab" or blood_type == "AB":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                    Oatmeal with sliced banana and almond butter.
                Lunch:
                    Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                    Fruit smoothie with berries, banana, and almond milk.
                Lunch:
                    Lentil soup with a side of whole-grain bread.
                Dinner:
                    tir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                    Whole grain toast with avocado and poached eggs.
                Lunch:
                    Chickpea and vegetable curry with basmati rice.
                Dinner:
                    Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                    Greek yogurt with honey and mixed berries.
                Lunch:
                    Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                    Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                    Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                    Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                    Smoothie with pineapple, kale, and coconut water.
                Lunch:
                    Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                    Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                    Cottage cheese with sliced peaches.
                Lunch:
                    Mixed greens salad with grilled salmon.
                Dinner:
                    Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "normal weight":        
        if blood_type == "o" or blood_type == "O":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Omelette with spinach and tomatoes.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Greek yogurt with sliced berries and a handful of almonds.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Smoothie with banana, spinach, and almond milk.
                Lunch:
                Quinoa bowl with mixed vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.


            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """
        elif blood_type == "a" or blood_type == "A":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.
            

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "b" or blood_type == "B":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Scrambled eggs with spinach and whole-grain toast.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Fruit smoothie with berries, banana, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "ab" or blood_type == "AB":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.
            

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        else:   
            print("Invalid blood type for the given category")     
    elif category_lower == "overweight":        
        if blood_type == "o" or blood_type == "O":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """
        elif blood_type == "a" or blood_type == "A":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "b" or blood_type == "B":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "ab" or blood_type == "AB":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        else:   
            print("Invalid blood type for the given category") 

    elif category_lower == "obese":        
        if blood_type == "o" or blood_type == "O":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """
        elif blood_type == "a" or blood_type == "A":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:   
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "b" or blood_type == "B":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        elif blood_type == "ab" or blood_type == "AB":
            diet = """ Dietary addice:
            general idea:
            

            meal plan:
            Monday:
                Breakfast:
                Oatmeal with sliced bananas and almonds.
                Lunch:
                Quinoa salad with mixed vegetables and grilled chicken.
                Dinner:
                Baked salmon with sweet potato and steamed broccoli.
            Tuesday:
                Breakfast:
                Smoothie with spinach, berries, and almond milk.
                Lunch:
                Lentil soup with a side of whole-grain bread.
                Dinner:
                Stir-fried tofu with brown rice and mixed vegetables.
            Wednesday:
                Breakfast:
                Whole grain toast with avocado and poached eggs.
                Lunch:
                Chickpea and vegetable curry with basmati rice.
                Dinner:
                Grilled shrimp with quinoa and sautéed kale.
            Thursday:
                Breakfast:
                Greek yogurt with honey and mixed berries.
                Lunch:
                Quinoa bowl with roasted vegetables and grilled chicken.
                Dinner:
                Baked cod with quinoa and roasted Brussels sprouts.
            Friday:
                Breakfast:
                Chia seed pudding with almond milk and topped with sliced kiwi.
                Lunch:
                Spinach and feta omelette with whole-grain toast.
                Dinner:
                Stir-fried tempeh with brown rice and asparagus.
            Saturday:
                Breakfast:
                Smoothie with pineapple, kale, and coconut water.
                Lunch:
                Quinoa salad with black beans, corn, and diced tomatoes.
                Dinner:
                Grilled chicken with quinoa and steamed asparagus.
            Sunday:
                Breakfast:
                Cottage cheese with sliced peaches.
                Lunch:
                Mixed greens salad with grilled salmon.
                Dinner:
                Stir-fried tofu with soba noodles and broccoli.

            Note:
            - Adjust portion sizes based on individual needs.
            - Include healthy snacks between meals if needed.
            - Stay hydrated with water throughout the day.     

            warning:
            These meal plans are general suggestions and may not suit everyone. 
            Individualized advice from healthcare professionals is crucial for 
            addressing specific health conditions and dietary needs.
            """    
        else:   
            print("Invalid blood type for the given category")      
        return diet if return_diet else ""   



def medical_advise(category, blood_type, return_advice=False):
    category_lower = category.lower()
    advice = ""

    if category_lower == "underweight":
        if blood_type == "o" or blood_type == "a" or blood_type == "b" or blood_type == "A" or blood_type == "B" or blood_type == "O" or blood_type == "ab" or blood_type == "AB":
            advice = """You are advised to:
            Increase Caloric Intake:
            Consume a variety of nutrient-dense foods to boost calorie intake.
            Include healthy fats such as avocados, nuts, seeds, and olive oil.

            Protein-Rich Foods:
            Include lean protein sources like poultry, fish, eggs, beans, and dairy to support muscle development.

            Frequent Meals:
            Eat smaller, more frequent meals throughout the day to increase overall calorie consumption.

            Strength Training:
            Engage in strength training exercises to build muscle mass.

            Nutrient-Rich Snacks:
            Snack on high-calorie, nutrient-dense foods like Greek yogurt, trail mix, and cheese.
            """
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "normal weight":
        if blood_type == "o" or blood_type == "a" or blood_type == "b" or blood_type == "A" or blood_type == "B" or blood_type == "O" or blood_type == "ab" or blood_type == "AB":
            advice = """You are advised to:
            Balanced Diet:
            Maintain a well-balanced diet with a mix of carbohydrates, proteins, and fats.
            Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats.

            Portion Control:
            Be mindful of portion sizes to avoid overeating.

            Regular Exercise:
            Incorporate regular physical activity for overall health and weight maintenance.
            """
        else:
            print("Invalid blood type for the given category")

    elif category_lower == "overweight":
        if blood_type == "o" or blood_type == "a" or blood_type == "b" or blood_type == "A" or blood_type == "B" or blood_type == "O" or blood_type == "ab" or blood_type == "AB":
            advice = """You are advised to:

            Control Calorie :
            Create a slight calorie deficit by consuming fewer calories than expended.

            Whole Foods:
            Choose whole, minimally processed foods to ensure nutrient intake.

            High-Fiber Foods:
            Include fiber-rich foods like fruits, vegetables, and whole grains to promote satiety.

            Lean Proteins:
            Opt for lean protein sources to support muscle maintenance during weight loss.

            Limit Added Sugars and Processed Foods:
            Reduce intake of sugary beverages, snacks, and highly processed foods.

            Regular Exercise:
            Engage in a combination of aerobic exercises and strength training for effective weight management.

                """
        else:
            print("Invalid blood type for the given category")
            

    elif category_lower == "obese":
        if blood_type == "o" or blood_type == "a" or blood_type == "b" or blood_type == "A" or blood_type == "B" or blood_type == "O" or blood_type == "ab" or blood_type == "AB":
            advice = """ You are advised to:
            Medical Supervision:
            -Seek medical supervision for a comprehensive weight management plan.

            Gradual Weight Loss:
            -Aim for gradual, sustainable weight loss rather than rapid changes.

            Balanced Diet:
            -Emphasize a well-balanced diet with appropriate portion control.

            Behavioral Changes:
            -Address behavioral aspects of eating, such as emotional eating or mindless snacking.

            Regular Physical Activity:
            -Incorporate regular and varied physical activities to support weight loss.

            Seek nutritional Counseling:
            -Consult with a registered dietitian for personalized dietary guidance.
                """
        else:
            print("Invalid blood type for the given category")
    else:
        print("Invalid category")
    return advice if return_advice else ""

def exercises(category,return_sports=False):
    category_lower = category.lower()
    sports=""
    if category_lower == "underweight":
        sports="""
        Monday:
            Cardio:
            20 minutes of brisk walking or jogging.
        Tuesday:
            Strength Training:
            Bodyweight exercises (e.g., push-ups, squats, lunges) - 3 sets of 12-15 reps each.
        Wednesday:
            Cardio:
            20 minutes of cycling or swimming.
        Thursday:
            Flexibility and Mobility:
            Yoga or stretching exercises - 30 minutes.
        Friday:
            Strength Training:
            Resistance training with light weights - 3 sets of 12-15 reps each.
        Saturday:
            Cardio:
            20 minutes of jump rope or dancing.
        Sunday:
            Rest or Light Activity:
            Walking or gentle stretching.

        Notes:
        Warm-up before each session and cool down afterward.
        Progress gradually and listen to your body.
        Include activities you enjoy to make fitness a sustainable lifestyle.   
        """

    elif category_lower == "normal weight":   
        sports="""
        Monday:
            Cardio:
            30 minutes of running or cycling.
        Tuesday:
            Strength Training:
            Full-body workout with weights - 4 sets of 10-12 reps each.
        Wednesday:
            Cardio and Interval Training:
            High-intensity interval training (HIIT) - 20 minutes.
        Thursday:
            Flexibility and Mobility:
            Pilates or yoga - 30 minutes.
        Friday:
            Strength Training:
            Target specific muscle groups with compound exercises - 4 sets of 10-12 reps each.
        Saturday:
            Cardio:
            30 minutes of swimming or rowing.
        Sunday:
            Active Recovery:
            Light hiking or cycling.

        Notes:
        Warm-up before each session and cool down afterward.
        Progress gradually and listen to your body.
        Include activities you enjoy to make fitness a sustainable lifestyle.
        """

    elif category_lower == "overweight":
        sports="""
        Monday:
            Cardio:
            30 minutes of brisk walking or elliptical training.
        Tuesday:
            Strength and Endurance Training:
            Circuit training with bodyweight exercises - 3 rounds.
        Wednesday:
            Cardio and Interval Training:
            HIIT workout - 20 minutes.
        Thursday:
            Flexibility and Mobility:
            Yoga or stretching - 30 minutes.
        Friday:
            Strength Training:
            Moderate weight lifting with focus on form - 4 sets of 10-12 reps each.
        Saturday:
            Cardio:
            30 minutes of cycling or swimming.
        Sunday:
            Active Recovery:
            Light yoga or walking.

        Notes:
        Warm-up before each session and cool down afterward.
        Progress gradually and listen to your body.
        Include activities you enjoy to make fitness a sustainable lifestyle.
        """

    elif category_lower == "obese":
        sports="""
        Monday:
            Low-Impact Cardio:
            30 minutes of water aerobics or stationary cycling.
        Tuesday:
            Strength and Stability:
            Seated or chair exercises focusing on stability - 3 sets of 12-15 reps.
        Wednesday:
            Low-Impact Cardio:
            20 minutes of walking or recumbent cycling.
        Thursday:
            Flexibility and Mobility:
            Gentle stretching or chair yoga - 30 minutes.
        Friday:
            Strength and Endurance:
            Resistance band exercises for upper and lower body - 3 sets of 12-15 reps.
        Saturday:
            Low-Impact Cardio:
            30 minutes of swimming or aquatic exercises.
        Sunday:
            Active Recovery:
            Light stretching or a leisurely walk.

        Notes:
        Warm-up before each session and cool down afterward.
        Progress gradually and listen to your body.
        Include activities you enjoy to make fitness a sustainable lifestyle.
        """

    else:
        print("Invalid category")
    return sports if return_sports else ""

# Create a Patient instance and run the application
patient = Patient()
patient.run_application()
