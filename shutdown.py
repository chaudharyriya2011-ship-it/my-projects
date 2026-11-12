choice = input("Enter your choice for shutting down (yes/no): ")
def shutdown(choice):
    if choice == "yes":
        print("Shutting down")
    elif choice == "no":
        print("Abort shutdown")
    else:
        print("sorry")
shutdown(choice)