my_symptom = []
Fe = input("Do you have a fever? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Fe == "a" or Fe == "Yes":
    Fe = 5
    my_symptom.append(Fe)
    print("Thank you")
    print("\n")
elif Fe == "c" or Fe == "Sometimes":
    Fe = 1
    my_symptom.append(Fe)
    print("Thank you")
    print("\n") 
else:
    Fe = 0
    my_symptom.append(Fe)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Fa = input("Do you feel fatigue? \na. Yes \nb. No \nAnswer:  ")
if Fa == "a" or Fa == "Yes":
    Fa = 2
    my_symptom.append(Fa)
    print("Thank you")
    print("\n")
else:
    Fa = 0
    my_symptom.append(Fa)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Co = input("Do you cough often? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Co == "a" or Co == "Yes":
    Co = 5
    my_symptom.append(Co)
    print("Thank you")
    print("\n")
elif Co == "c" or Co == "Sometimes":
    Co = 1
    my_symptom.append(Co)
    print("Thank you")
    print("\n")      
else:
    Co = 0
    my_symptom.append(Co)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Sn = input("Are you sneezing often? \na. Yes \nb. No \nAnswer:  ")
if Sn == "a" or Sn == "Yes":
    Sn = 2
    my_symptom.append(Sn)
    print("Thank you")
    print("\n")
else:
    Sn = 0
    my_symptom.append(Sn)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Ap = input("Do you feel aches and pains in your body? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Ap == "a" or Ap == "Yes":
    Ap = 2
    my_symptom.append(Ap)
    print("Thank you")
    print("\n")
elif Ap == "c" or Ap == "Sometimes":
    Ap = 1
    my_symptom.append(Ap)
    print("Thank you")
    print("\n")      
else:
    Ap = 0
    my_symptom.append(Ap)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
St = input("Do you have a sore throat? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if St == "a" or St == "Yes":
    St = 2
    my_symptom.append(St)
    print("Thank you")
    print("\n")
elif St == "c" or St == "Sometimes":
    St = 1
    my_symptom.append(St)
    print("Thank you")
    print("\n")      
else:
    St = 0
    my_symptom.append(St)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Rn = input("Do you have a runny or stuffy nose? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Rn == "a" or Rn == "Yes":
    Rn = 2
    my_symptom.append(Rn)
    print("Thank you")
    print("\n")
elif Rn == "c" or Rn == "Sometimes":
    Rn = 1
    my_symptom.append(Rn)
    print("Thank you")
    print("\n")      
else:
    Rn = 0
    my_symptom.append(Rn)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Dh = input("Do you have diarrhea? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Dh == "a" or Dh == "Yes":
    Dh = 2
    my_symptom.append(Dh)
    print("Thank you")
    print("\n")
elif Dh == "c" or Dh == "Sometimes":
    Dh = 1
    my_symptom.append(Dh)
    print("Thank you")
    print("\n")      
else:
    Dh = 0
    my_symptom.append(Dh)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Ha = input("Do you have a headache? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Ha == "a" or Ha == "Yes":
    Ha = 2
    my_symptom.append(Ha)
    print("Thank you")
    print("\n")
elif Ha == "c" or Ha == "Sometimes":
    Ha = 1
    my_symptom.append(Ha)
    print("Thank you")
    print("\n")      
else:
    Ha = 0
    my_symptom.append(Ha)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Sb = input("Do you feel shortnes of breath? \na. Yes \nb. No \nc. Sometimes \nAnswer:  ")
if Sb == "a" or Sb == "Yes":
    Sb = 5
    my_symptom.append(Sb)
    print("Thank you")
    print("\n")
elif Sb == "c" or Sb == "Sometimes":
    Sb = 1
    my_symptom.append(Sb)
    print("Thank you")
    print("\n")      
else:
    Sb = 0
    my_symptom.append(Sb)
    print("Thank you")
    print("\n")
print(sum(my_symptom))
print("\n")
Final_sym = sum(my_symptom)
if Final_sym > 19:
    print("You have the Corona Virus. Please call  112 now")
elif 11 <= Final_sym <= 18:
    print("You have a flu. Please see your doctor soon")
elif Final_sym <= 10 :
    print("You have a cold. Please see your doctor soon")
else:
    print("Please see your doctor for other diagnosis")