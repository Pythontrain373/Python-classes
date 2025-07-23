def shutdown():
    ans=input("Do you need to shutdown the computor: ")
    if ans=="yes":
        print("Shutting down")
    elif ans=="no":
        print("Abort shutdown")
    else:
        print("Sorry")
shutdown()