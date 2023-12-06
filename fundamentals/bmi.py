import time

print()
print("Welcome to BodyMath: A smart BMI calculator")
time.sleep(3)
print()
print("The all-in-one health and wellness app designed to empower individuals on their weight management journey.") 
print("This innovative app seamlessly combines BMI tracking with personalized insights based on blood type,")
print("creating a holistic approach to achieving and maintaining a healthy weight.")
time.sleep(5)

class Patient:
    def __init__(self, name="", gender="", blood_type="", age=""):
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
        diet=""

        while True:
            print("\n1. Add patient\n2. Enter your details for BMI calculation\n3. Display patient information\n4. Medical advice\n5. Dietary advice\n6. Access your exercise routine\n7. Meet professional personnels and nutritionists\n8. Save and Exit")
            choice = input("Enter your choice (1-5): ")

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
                print(dietary_advise)
            elif choice == "6":
                print(exercice_routine)
            elif choice == "7":
                print(doctor)
            elif choice == "8":
                self.save_to_file(bmi, category, advice)
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

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

                
        else:
            print("Invalid blood type for the given category")
            """

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

# Create a Patient instance and run the application
patient = Patient()
patient.run_application()