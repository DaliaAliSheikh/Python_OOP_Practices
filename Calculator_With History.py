class Calculator:

    def __init__(self):
        self.result = []
        while True:
            operation = input(
                "ادخل :/ضرب /قسمة/سجل/مسح /الجمع/طرح /خروج:"
            )
            if operation == "الجمع":
                first_num = float(input("ادخل الرقم الاول:"))
                second_num = float(input("ادخل الرقم التاني:"))
                total = first_num + second_num
                self.result.append(
                    f"الناتج هو {first_num} + {second_num} ={total} "
                )
                print(" الناتج هو", total)
            elif operation == "طرح":
                first_num = float(input("ادخل الرقم الاول:"))
                second_num = float(input("ادخل الرقم التاني:"))
                difference = first_num - second_num
                self.result.append(
                    f"الناتج هو{first_num} - {second_num} ={difference} "
                )
                print(" الناتج ", difference)
            elif operation == "ضرب":
                first_num = float(input("ادخل الرقم الاول:"))
                second_num = float(input("ادخل الرقم التاني:"))
                product = first_num * second_num
                self.result.append(
                    f"الناتج هو{first_num} * {second_num} ={product} "
                )
                print(" الناتج", product)
            elif operation == "قسمة":
                first_num = float(input("ادخل الرقم الاول:"))
                second_num = float(input("ادخل الرقم التاني:"))
                if second_num == 0:
                    print("لا يمكن القسمة على صفر")
                else:
                    quotient = first_num / second_num
                    self.result.append(
                        f" الناتج هو{first_num} /{second_num} ={quotient} "
                    )
                    print(" الناتج", quotient)
            elif operation == "سجل":
                print(" سجل العمليات هو")
                if len(self.result) == 0:
                    print("مافي عمليات لسه")
                else:
                    for record in self.result:
                        print(record)
            elif operation == "مسح":
                self.result = []
                print("تم مسح السجل بنجاح ")
            elif operation == "خروج":
                print(" مع السلامة")
                break


k = Calculator()
