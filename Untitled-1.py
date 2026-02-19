try:
    user_input = input("Enter the age (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
    else:
        age = int(user_input)
        if age < 18:
            print("You are a minor.")
        elif 18 <= age < 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
