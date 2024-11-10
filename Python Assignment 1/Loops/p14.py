while True:
    user_input = input("Enter something (type 'exit' to break the loop): ")
    if user_input == "exit":
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")