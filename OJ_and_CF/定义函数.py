def calculate_BMI(weight,height):
    BMI = weight / height **2
    if BMI <=18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif  BMI <= 30:
        category = "偏胖"
    print(str(category))
calculate_BMI(11,22)