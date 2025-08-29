# Project1 : skill tracker mini project
name = input("Enter Your Name : ")
skills = input("Enter your Skills (comma sapreted value) e.g. html,css,js,python  etc.. : ").split(",")
def skillPrinter(name,skills):
    print(f"Hello, {name}")
    print("Your Skills are : ")
    for skill in skills:
        print(skill)
    print("Keep Learning:)")

skillPrinter(name=name,skills=skills)




