from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect,HttpResponse
from reglog.models import registration, student_details_1,student_details_2,all_details
import pdb
def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'reglog/login.html')
def logout_view(request):
    return render(request, 'reglog/login.html')
def register_view(request):
    return render(request, 'reglog/register.html')

def save_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")
        phone = request.POST.get("phno")
        email = request.POST.get("email")
        con_password = request.POST.get("con_pass")
        value = registration(name = name, password= password, con_password= con_password,phone=phone,email=email)
        
        auth = registration.objects.filter(email=email).values("email")
        auth_1 = registration.objects.filter(phone=phone).values("phone")
        # pdb.set_trace() 
        if name == '' and password == '' and email == '' and phone == '':
            massage = {"massage": "All details are required !!!!"}
            return render(request,'reglog/register.html',massage)
        elif name == '':
            massage = {"massage": "College Name is required !!!!"}
            return render(request,'reglog/register.html',massage)
        elif password == '':
            massage = {"massage": "password is required !!!!"}
            return render(request,'reglog/register.html',massage)
        elif phone == '':
            massage = {"massage": "Phone No. is required !!!!"}
            return render(request,'reglog/register.html',massage)
        elif email == '':
            massage = {"massage": "email is required !!!!"}
            return render(request,'reglog/register.html',massage)
        
        else:
            if len(password) < 8:
                massage = {"massage": "Password have minimum 8 charecters !!!!"}
                return render(request,'reglog/register.html',massage)   
            if password != con_password:
                massage = {"massage": "Password not match!!!!"}
                return render(request,'reglog/register.html',massage)  
            if len(phone) != 10:
                massage = {"massage": "Please Enter Valid Phone No. !!!!"}
                return render(request,'reglog/register.html',massage)
            elif not phone.isnumeric():
                
                massage = {"massage": "Please Enter Valid Phone No. !!!!"}
                return render(request,'reglog/register.html',massage)
            if email:
                a,b,c = 0,0,0
                if len(email) >= 6:
                    if email[0].isalpha():
                        if ("@" in email) and (email.count("@")==1):
                            # pdb.set_trace()
                            if (email[-4] == '.') ^ (email[-3] == '.'):
                                for i in email:
                                    if i == i.isspace():
                                        a=1
                                    elif i.isalpha():
                                        if i == i.upper():
                                            b = 1
                                          
                                    elif i.isdigit():
                                        continue
                                    elif i == '_' or i == '.' or i == '@':
                                        continue
                                    else:
                                        c = 1
                                # pdb.set_trace()
                                if a == 1 or b == 1 or c == 1:
                                    
                                    massage = {"massage": "Wrong email !!!!"}
                                    return render(request,'reglog/register.html',massage)
                                else:
                                    if not auth.exists() and not auth_1.exists():
                                        if email.endswith(".com"):
                                            value.save()
                                            return render(request,'reglog/login.html')
                                        elif email.endswith(".in"):
                                            value.save()
                                            return render(request,'reglog/login.html')
                                        else:
                                            massage = {"massage": "Wrong email !!!!"}
                                            return render(request,'reglog/register.html',massage)
                                    elif auth_1.exists():
                                        massage = {"massage": "Phone No. is already exist !!!!"}
                                        return render(request,'reglog/register.html',massage)
                                    elif auth.exists():
                                        massage = {"massage": "Email is already exist !!!!"}
                                        return render(request,'reglog/register.html',massage)
                                    value.save()
                                    return render(request,'reglog/login.html')
                            else:
                                massage = {"massage": "Wrong email !!!!"}
                                return render(request,'reglog/register.html',massage)
                        else:                           
                            massage = {"massage": "Wrong email !!!!"}
                            return render(request,'reglog/register.html',massage)
                    else: 
                        
                        massage = {"massage": "Wrong email !!!!"}
                        return render(request,'reglog/register.html',massage)
                else:
                    
                    massage = {"massage": "Wrong email !!!!"}
                    return render(request,'reglog/register.html',massage)
                    
        
email=""      
def com_log(request):
    if request.method == "POST":
        global email
        email = request.POST.get("email")
        password = request.POST.get("pass")
        auth = registration.objects.filter(email=email).values('email','password','name')
        
        if not auth.exists():
             massage = {"massage": "your account does not exist!!!"}
             return render(request,"reglog/login.html",massage)
        elif auth[0]['password'] == password:
            intro = {"intro": auth[0]['name']}
            
            return render(request,"profile/collegeprofile.html",intro)
        else:
            massage = {"massage": "password is invalid..!"}
            return render(request,"reglog/login.html",massage)
        
def onetofive_view(request):
    # pdb.set_trace()
    global email
    if request.method == "POST":
        reemail = registration.objects.get(email = email)
        roll_number = request.POST.get("roll_number")       
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        class_student = request.POST.get("class")
        maths = request.POST.get("maths")        
        hindi = request.POST.get("hindi")
        english = request.POST.get("english")
        enviromental_science = request.POST.get("enviromentalscience")

        auth_1 = all_details.objects.filter(email1=reemail).values('roll_number', 'email1')
        
        
            # pdb.set_trace()
        if roll_number=="" and first_name=="" and last_name=="" and class_student=="" and maths=="" and hindi=="" and english=="" and enviromental_science=="" :
            massage = {"massage" : "Please fill all fields"}
            return render(request, 'profile/insert/1_to_5.html',massage)
        elif "" in (roll_number,first_name,last_name,class_student,maths,hindi,english,enviromental_science):
            massage = {"massage" : "Please fill all fields"}
            return render(request, 'profile/insert/1_to_5.html',massage)
        elif  not first_name.isalpha() or not last_name.isalpha():
            # pdb.set_trace()
            massage = {"massage" : "Enter valid name !!!"}
            return render(request, 'profile/insert/1_to_5.html',massage)
        elif int(class_student) < 1 or int(class_student) > 5:
            massage = {"massage" : "Enter valid class !!!"}
            return render(request, 'profile/insert/1_to_5.html',massage)
        else:
            for i in (maths,hindi,english,enviromental_science):
                if int(i) < 0 or int(i) > 100:
                    massage = {"massage" : "Enter valid marks !!!"}
                    return render(request, 'profile/insert/1_to_5.html',massage)
                count_roll = False
            if not auth_1.exists():
                all_details.objects.create(roll_number=roll_number,email1=reemail)
                roll_number_refer = all_details.objects.get(roll_number=roll_number)
                student_details_1.objects.create( roll_number=roll_number_refer ,first_name = first_name, last_name=last_name, class_student=class_student, maths=maths, hindi=hindi, english=english,enviromental_science=enviromental_science)
                massage = {"massage" : "Inserted"}
                return render(request, 'profile/insert/1_to_5.html',massage)
            elif auth_1.exists():
                count_roll = False
                for i in range(len(auth_1)):               
                    if auth_1[i]['roll_number'] == roll_number:                   
                        count_roll = True
                        break
                if count_roll is True:
                    # pdb.set_trace()
                    massage = {"massage" : "Roll_number is already exist for this college !!!"}
                    return render(request, 'profile/insert/1_to_5.html',massage)
                all_details.objects.create(roll_number=roll_number,email1=reemail)
                roll_number_refer = all_details.objects.get(roll_number=roll_number, email1= reemail)
                student_details_1.objects.create( roll_number=roll_number_refer ,first_name = first_name, last_name=last_name, class_student=class_student, maths=maths, hindi=hindi, english=english,enviromental_science=enviromental_science)
                massage = {"massage" : "Inserted"}
                return render(request, 'profile/insert/1_to_5.html',massage)
        return render(request, 'profile/insert/1_to_5.html')
    return render(request, 'profile/insert/1_to_5.html')
def sixtoten_view(request):
    global email
    if request.method == "POST":
        reemail = registration.objects.get(email = email)
        roll_number = request.POST.get("rollnumber")       
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        class_student = request.POST.get("class")
        maths = request.POST.get("maths")        
        hindi = request.POST.get("hindi")
        english = request.POST.get("english")
        science = request.POST.get("science")
        social_studies = request.POST.get("socialstudies")
        
        auth_1 = all_details.objects.filter(email1=reemail).values('roll_number', 'email1')
        # pdb.set_trace() 
        if roll_number=="" and first_name=="" and last_name=="" and class_student=="" and maths=="" and hindi=="" and english=="" and science=="" and social_studies=="":
            massage = {"massage" : "Please fill all fields"}
            return render(request, 'profile/insert/6_to_10.html',massage)
        elif "" in (roll_number,first_name,last_name,maths,hindi,english,science,social_studies):
            massage = {"massage" : "Please fill all fields"}
            return render(request, 'profile/insert/6_to_10.html',massage)
        elif  not first_name.isalpha() or not last_name.isalpha():
            
            massage = {"massage" : "Enter valid name !!!"}
            return render(request, 'profile/insert/6_to_10.html',massage)
        elif int(class_student) < 5 or int(class_student) > 10:
            massage = {"massage" : "Enter valid class !!!"}
            return render(request, 'profile/insert/6_to_10.html',massage)
        else:
            for i in (maths,hindi,english,science,social_studies):
                if int(i) < 0 or int(i) > 100: 
                    massage = {"massage" : "Enter valid marks !!!"}
                    return render(request, 'profile/insert/6_to_10.html',massage)
                count_roll = False
            if not auth_1.exists():
                all_details.objects.create(roll_number=roll_number,email1=reemail)
                roll_number_refer = all_details.objects.get(roll_number=roll_number)
                student_details_2.objects.create( roll_number=roll_number_refer ,first_name = first_name, last_name=last_name, class_student=class_student, maths=maths, hindi=hindi, english=english, science= science, social_studies=social_studies)
                massage = {"massage" : "Inserted"}
                return render(request, 'profile/insert/6_to_10.html',massage)
            elif auth_1.exists():
                count_roll = False
                for i in range(len(auth_1)):               
                    if auth_1[i]['roll_number'] == roll_number:                   
                        count_roll = True
                        break
                if count_roll is True:
                    
                    massage = {"massage" : "Roll_number is already exist for this college !!!"}
                    return render(request, 'profile/insert/6_to_10.html',massage)
                
                all_details.objects.create(roll_number=roll_number,email1=reemail)
                # pdb.set_trace()
                roll_number_refer = all_details.objects.get(roll_number=roll_number)
                # pdb.set_trace()
                student_details_2.objects.create( roll_number=roll_number_refer ,first_name = first_name, last_name=last_name, class_student=class_student, maths=maths, hindi=hindi, english=english, science= science, social_studies=social_studies)
                massage = {"massage" : "Inserted"}
                return render(request, 'profile/insert/6_to_10.html',massage)
        return render(request, 'profile/insert/6_to_10.html')
    return render(request, 'profile/insert/6_to_10.html')

def profile_view(request):
    return render(request, 'profile/profile.html')
def insert1(request):
    return render(request, 'profile/insert.html')

def search_view(request):
    if request.method == "POST":
        global email
        reemail = registration.objects.get(email = email)
        roll_number = request.POST.get("rollnumber")
        check = all_details.objects.filter(email1=reemail).values("roll_number")
        
        count_roll_number= False
        for i in range(len(check)):

            if check[i]["roll_number"] == roll_number:
                count_roll_number = True
        if count_roll_number is True:
                search = all_details.objects.get(roll_number=roll_number, email1=reemail)
                search2 = None
                s = (student_details_1,student_details_2)
                 
                for i in range(len(s)):
                    if i == 0:
                        search2 = s[i].objects.filter(roll_number=search).values("first_name","last_name","class_student","maths","hindi","english","enviromental_science")
                        if search2.exists():
                            # pdb.set_trace()
                            massage0 = {"massage0" : search2}
                            return render(request, 'profile/search.html',massage0)
                        
                    elif i == 1:
                        search2 = s[i].objects.filter(roll_number=search).values("first_name","last_name","class_student","maths","hindi","english","science","social_studies")
                        if search2.exists():
                            massage1 = {"massage1" : search2}
                            return render(request, 'profile/search.html',massage1)
                      
        else:    
            massage = {"massage" : "Roll number is not exist !!!"}
            return render(request, 'profile/search.html',massage)
    return render(request, 'profile/search.html')

def update_result(request,id):
    if request.method == "POST":
              
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        class_student = request.POST.get("class")
        maths = request.POST.get("maths")        
        hindi = request.POST.get("hindi")
        english = request.POST.get("english")
        enviromental_science = request.POST.get("environmentalscience")
        science = request.POST.get("science")
        social_studies = request.POST.get("socialstudies")
        s = (student_details_1,student_details_2)
                 
        for i in range(len(s)):
            if i == 0:
                search2_update = s[i].objects.filter(id = id).values("first_name","last_name","class_student","maths","hindi","english","enviromental_science")                
                if search2_update.exists():   
                    x = s[i].objects.get(id=id)                    
                    x.first_name = first_name
                    x.last_name = last_name  
                    x.class_student  = class_student  
                    x.maths = maths 
                    x.hindi = hindi  
                    x.english=english
                    x.enviromental_science = enviromental_science
                    x.save()                      
                    # updated = {"updated" : "updated"}
                    return redirect('/update/')              
            elif i == 1:
                search2_update = s[i].objects.filter(id = id).values("id","first_name","last_name","class_student","maths","hindi","english","science","social_studies")
                if search2_update.exists():   
                    x = s[i].objects.get(id=id)                    
                    x.first_name = first_name
                    x.last_name = last_name  
                    x.class_student  = class_student  
                    x.maths = maths 
                    x.hindi = hindi  
                    x.english=english
                    x.science = science
                    x.social_studies=social_studies
                    x.save()                      
                    # updated = {"updated" : "updated"}
                    return redirect('/update/')
                   
def update_view(request):
    if request.method == "POST":
        global email, search_update, search2_update
        reemail = registration.objects.get(email = email)
        roll_number = request.POST.get("rollnumber")
        check = all_details.objects.filter(email1=reemail).values("roll_number")
        
        count_roll_number= False
        for i in range(len(check)):

            if check[i]["roll_number"] == roll_number:
                count_roll_number = True
        if count_roll_number is True:
                search_update = all_details.objects.get(roll_number=roll_number, email1=reemail)
                
                s = (student_details_1,student_details_2)
                 
                for i in range(len(s)):
                    if i == 0:
                        search2_update = s[i].objects.filter(roll_number=search_update).values("first_name","last_name","class_student","maths","hindi","english","enviromental_science")
                        if search2_update.exists():
                           
                            massage0 = {"massage0" : search2_update}
                            return render(request, 'profile/update.html',massage0)
                        
                    elif i == 1:
                        search2_update = s[i].objects.filter(roll_number=search_update).values("id","first_name","last_name","class_student","maths","hindi","english","science","social_studies")
                        if search2_update.exists():
                            # m1 = s[i].objects.get(id)
                            massage1 = {"massage1" : search2_update}
                            # pdb.set_trace()
                            return render(request, 'profile/update.html',massage1)
                # pdb.set_trace()       
        else:    
            massage = {"massage" : "Roll number is not exist !!!"}
            return render(request, 'profile/update.html',massage)
    return render(request, 'profile/update.html')
def delete_view(request):
    if request.method == "POST":
        global email
        reemail = registration.objects.get(email = email)
        roll_number = request.POST.get("rollnumber")
        check = all_details.objects.filter(email1=reemail).values("roll_number")
        
        count_roll_number= False
        for i in range(len(check)):

            if check[i]["roll_number"] == roll_number:
                count_roll_number = True
        if count_roll_number is True:
                search = all_details.objects.get(roll_number=roll_number, email1=reemail)
                # search2 = None
                s = (student_details_1,student_details_2)
                for i in range(len(s)):
                    if i == 0:
                        search2 = s[i].objects.filter(roll_number=search)
                        if search2.exists():
                            
                            search2.delete()
                            break
                    elif i == 1:
                        search2 = s[i].objects.filter(roll_number=search).values("first_name","last_name","class_student","maths","hindi","english","science","social_studies")
                        if search2.exists():
                            break
                search.delete()                
                massage = {"massage" : "deleted"}
                return render(request, 'profile/delete.html',massage)
    return render(request, 'profile/delete.html')
def showall_view(request):
    return render(request, 'profile/showall.html')





def searchdetails_view(request, id):
                s = (student_details_1,student_details_2)
                 
                for i in range(len(s)):
                    if i == 0:
                        search2 = s[i].objects.filter(roll_number=id).values("first_name","last_name","class_student","maths","hindi","english","enviromental_science")
                        # pdb.set_trace()
                        if search2.exists():
                            
                            massage0 = {"massage0" : search2}
                            return render(request,'profile/showall/details.html',massage0)
                        
                    elif i == 1:
                        search2 = s[i].objects.filter(roll_number=id).values("first_name","last_name","class_student","maths","hindi","english","science","social_studies")
                        if search2.exists():
                            massage1 = {"massage1" : search2}
                            return render(request,'profile/showall/showsixtoten.html',massage1)







def showonetofive_view(request):
    global email
    reemail = registration.objects.get(email = email)
    check = all_details.objects.filter(email1=reemail).values("id","roll_number","email1")
    # pdb.set_trace()
    show = {"show" : check}
    return render(request,'profile/showall/showonetofive.html',show)
def showsixtoten_view(request):
    return render(request,'profile/showall/showsixtoten.html')

def eleven_twelve_view(request):
    return render(request, 'profile/insert/11_or_12.html')

def Mathscience_view(request):
    return render(request, 'profile/insert/Select_school_field/Mathscience.html')
def Biology_view(request):
    return render(request, 'profile/insert/Select_school_field/Biology.html')
def Commerce_view(request):
    return render(request, 'profile/insert/Select_school_field/Commerce.html')
def Arts_view(request):
    return render(request, 'profile/insert/Select_school_field/Arts.html')
def Agriculture_view(request):
    return render(request, 'profile/insert/Select_school_field/Agriculture.html')


def Computerscience_view(request):
    return render(request, 'profile/insert/Engineer/Computerscience.html')

def Informationtechnology_view(request):
    return render(request, 'profile/insert/Engineer/Informationtechnology.html')
def Mechenical_view(request):
    return render(request, 'profile/insert/Engineer/Mechenical.html')
def Civil_view(request):
    return render(request, 'profile/insert/Engineer/Civil.html')
def Electronic_view(request):
    return render(request, 'profile/insert/Engineer/Electronic.html')

def BCominAccountancy_view(request):
    return render(request, 'profile/insert/Bcom/BCominAccountancy.html')
def BCominBankingandFinance_view(request):
    return render(request, 'profile/insert/Bcom/BCominBankingandFinance.html')
def CominBusinessAdministration_view(request):
    return render(request, 'profile/insert/Bcom/CominBusinessAdministration.html')
def BCominE_Commerce_view(request):
    return render(request, 'profile/insert/Bcom/BCominE_Commerce.html')
def BCominFinance_view(request):
    return render(request, 'profile/insert/Bcom/BCominFinance.html')

def BScComputerscience_view(request):
    return render(request, 'profile/insert/BSc/BScComputerscience.html')
def BScInformationtechnology_view(request):
    return render(request, 'profile/insert/BSc/BScInformationtechnology.html')
def BScPhysics_view(request):
    return render(request, 'profile/insert/BSc/BScPhysics.html')
def BScNursing_view(request):
    return render(request, 'profile/insert/BSc/BScNursing.html')
def BScAgriculture_view(request):
    return render(request, 'profile/insert/BSc/BScAgriculture.html')

