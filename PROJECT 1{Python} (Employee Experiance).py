                #PROJECT 1{Python} (Employee Experiance)
#قائمتان
#الاولى تحتوى على سنين الخبرة للموظفين
#الثانية تحتوي على مرتبات الموظفين
#فلو عندى موظف جديد مش موجود بالقائمة سيقوم بتقدير مرتب الموظف الجديد
#2 lists
#1-years of employee's experiance. 2- employee's salaries
#years of experiance
experiance=[1,2,3,5,8,9,11,22]
salaries=[3000,3500,4000,4500,5000,6000,8000,12000]
#قبل ما اكمل الكود محتاج اتاكد ان طول ال2lists متساوى وان العناصر لل2lists من نفس نوع الtype
#عشان اتاكد من طول الlist متساوى
len(salaries)
len(experiance)
#عشان اتاكد من ان عناصر اى رقم داخل الlist الاولى او الثانية من نفس النوع
type(salaries[0])
type(experiance[1])
#دلوقتى انا عايز اعمل كود يطلب من اليوزر انة يدخل اسم الموظف الجديد وسنين خبرتة
newemployee=input("plz enter the new employee name: ")
newemployee_exp=float(input("plz enter the new employee experiance: "))
#نتاكد من نوع الداتا اللى تم ادخالها من اليوزر لكل variable
type(newemployee)
type(newemployee_exp)
#دلوقتى مطلوب منى انى اخد رقم newemployee_exp واشوفة جوة الlist بتاعة الexpriance لو موجود يطلع ليا المرتب عالطول المقابل لة فى الlist بتاعة الsalaries ولو مش موجود يطلع ليا range للرقم ويجيب منها range من الlist بتاعة الsalaries
#دلوقتى انا محتاج اليوزر يدخل ليا سنين الخبرة وبعدين اخلى المدخل دة يلف جوة الكود ولو لقى الرقم من ضمن الارقام اللى فى الlist بتاعة experiance يظهرلى عالطول المفروض ياخد مرتب قد اية من الlist بتاعة الsalaries
#طيب لو مالاقهوش يبقى يجيب الrange من الlist بتاعة الexperiance وبعدين يجيب الrange من الlist بتاعة الsalaries ويظهر لليوزر المفروض يقبض كام
#بمعنى لو دخل رقم 4 ورقم 4 مش موجود فى الlist بتاعة الexperiance يبقى هيجيب الrange من الخبرة ويظهر لليوزر range المرتب
#هنعرف 2 متغير متغير للحد الادنى(عشان لو كتبت رقم مش موجود وهيجيب range ومتغير للحد الاعلى)
#متغير الحد الادنى
lower_exp=0
upper_exp=0
#تمام دلوقتى انا عايز اعمل كود يلف جوة الكود عشان يجيب الحد الادنى 
#عشان يلف جوة الlist بتاعة الexperiance
for i in experiance:
#عشان يبص على عدد سنين الخبرة الخاصة بالموظف الجديد ويطلع ليها الحد الادنى
    if i<newemployee_exp:
#هيبص على كل رقم جوة الlist بتاعة الexperiance ..رقم,رقم..ويتاكد ان سنين خبرة الموظف الجديد اكبر من كل رقم داخل الlist..ولو لقى ان سنين خبرة الموظف الجديد اصغر من رقم داخل الlist...ساعتها هيعمل اية؟
        lower_exp=i
#لو لقى رقم اصغر من سنين خبرة الموظف الجديد هيخزن الرقم الاصغر دة عالطول فى الlower ودة هيبقى الحد الادنى
for i in experiance:
#عشان يبص على عدد سنين الخبرة الخاصة بالموظف الجديد ويطلع ليها الحد الاعلى
    if i>newemployee_exp:
#هيبص على كل رقم جوة الlist بتاعة الexperiance ..رقم,رقم..ويتاكد ان سنين خبرة الموظف الجديد اصغر من كل رقم داخل الlist..ولو لقى ان سنين خبرة الموظف الجديد اكبر من رقم داخل الlist...ساعتها هيعمل اية؟
        upper_exp=i
#يعنى اية كل دة:بمعنى ان لو دخلت عدد سنين خبرة الموظف الجديد=6 سنين..هيخزن فى الlower الرقم 5 , وهيخزن فى الupper الرقم 8 من الlist بتاعة الexperiance
#هقولة دلوقتى يطبعلى الرقم الاعلى وبعدين هطلب منة يخرج برة الloop
        print(upper_exp)
        break
#دلوقتى انا عايز اخلية يبص على رقم الindex فى الlist بتاعة الexperiance واقولة انة بالرقم بتاع الindex دة قارنة بالرقم بتاع الindex الخاص بالlist بتاع الsalaries
#تمام دلوقتى انا عايز اقولة لو جيبت الindex بتاعة الحد الادنى فى الlist بتاعة الexpriance هاتلى نفس الindex فى الراتب الاقل منة..ونفس النظام فى الحد الاعلى..هنعملها ازاى؟
lower_salary=salaries[experiance.index(lower_exp)]
#هعمل منغير جديد للحد الادنى فى الsalaries وهقولة لما تجيب الlower هات الindex بتاعة وحط الindex دة فى الحد الادنى للاجور ك index
heigher_salary=salaries[experiance.index(upper_exp)]        
#دلوقتى هنجيب الراتب بتاع الموظف الجديد
salaryofthenewemployee=str((lower_salary+heigher_salary)/2)
print("the salary of the new employee is: " +salaryofthenewemployee + "Dollars" )