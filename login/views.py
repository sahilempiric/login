from django.shortcuts import redirect, render  
from .models import user_data
import re  
from django.contrib import messages
    
def registration_view(request):
    # if request('No ! -------------------------',request.POST['age']) 
    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        pass_WORD = request.POST['password']
        pass_WORD1 = request.POST['password']

        context = {
            'user_name' : user_name,
            'email' : email,
            'first_name' : first_name,
            'last_name' : last_name
        }

        if user_name != None:
            # m_username = user_data.objects.get(username = user_name)
            # m_email = user_data.objects.get(email=email)
             

            if first_name != None:
                if last_name != None  :
                    if email != None :
                        if pass_WORD != None:
                            pass_WORD = request.POST['password']
                            pass_WORD1 = request.POST['password1']
                            
                            # calculating the length
                            length_error = len(pass_WORD) < 8

                            # searching for digits
                            digit_error = re.search(r"\d", pass_WORD) is None

                            # searching for uppercase
                            uppercase_error = re.search(r"[A-Z]", pass_WORD) is None

                            # searching for lowercase
                            lowercase_error = re.search(r"[a-z]", pass_WORD) is None

                            # searching for symbols
                            symbol_error = re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pass_WORD) is None

                            # overall result
                            pass_WORD_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
                            
                            # if m_username is not None :
                            #     pass_WORD_ok = False
                            print(pass_WORD_ok)
                            # if user_data.objects.get(email=email) :
                            #     pass_WORD_ok = False
                            if pass_WORD_ok == True :
                                if pass_WORD  == pass_WORD1:
                                    print('yes ! ---------------------worked')
                                    if user_data.objects.filter(username = user_name).exists():
                                        messages.error(request,"This username is already taken !")
                                        return render(request,'register.html',context) 
                                    else:
                                        if user_data.objects.filter(email=email).exists():
                                            messages.error(request,"This email is already taken !")
                                            return render(request,'register.html',context)
                                        else:
                                            pass_WORD = request.POST['password']
                                            user_data.objects.create(username = user_name, first_name = first_name , password = pass_WORD , last_name = last_name , email = email )
                                            messages.success(request,"you forms has been submited !")
                                            return render(request,'login.html',context) 
                                else:
                                    print('pass_WORD not match')
                                    messages.error(request,"Password is not Matching !")
                                    return render(request,'register.html',context)
                            else:
                                print('not best pass_WORD')
                                messages.error(request,"please provide us secure Password !")
                                return render(request,'register.html',context)
                        else:
                            print('no pass_WORD')
                            messages.error(request,"please provide us Password !")
                            return render(request,'register.html',context)
                    else:
                        print('no email')
                        messages.error(request,"please provide us Email !")
                        return render(request,'register.html',context)
                else:
                    print('no last name')
                    messages.error(request,"please provide us Last name !")
                    return render(request,'register.html',context)
            else :
                print('no first name')
                messages.error(request,"please provide us First name !")
                return render(request,'register.html',context)
        else:
            print('nousername')
            messages.error(request,"Please provide a username !")
            return render(request,'register.html',context)



    return render(request,'register.html')



def login_view(request):

    if request.method == "POST":
        user_mail = request.POST['user_mail']
        password = request.POST['password']
        # pipudi=user_data.objects.get(email=user_mail)
        # print(pipudi,'------------------------')
        if user_data.objects.filter(username = user_mail,password = password).exists()   :
            return redirect('dashboard')

        elif user_data.objects.filter(email=user_mail,password = password).exists() :
            return redirect('dashboard')

        else:
            print('user not found')
        return render(request,'login.html')
    else:
        return render(request,'login.html')
# or  user_data.objects.filter(email = user_mail).exists()



def home(request):
    return render(request,'dashbord.html')