class student:
    def __init__(self,kod,name,surname,mail,phone):
        self.kod = kod
        self.name= name
        self.surname= surname
        self.mail=mail
        self.phone= phone
    def showinfo(self,kod,name,surname,mail,phone):
       print(self.kod, self.name,self.surname, self.mail,self.phone)
       
arr=[]


for i in range(0,10):
    kod = int(input("kodu daxil edin: "))
    name = input("ad yazin :")
    surname = input("soyad yazin :")
    mail =  input("mail daxil edin: ")
    phone = input("nomre daxil edin: ")
    telebe= student(kod,name,surname,mail,phone)
    arr.append(telebe)
    print(arr[0].showinfo(kod,name,surname,mail,phone))
    #kod
    if kod in range(99,1000) :
        print("duzdu")
    else:
        print("xahiş edirəm üç rəqəm daxil edin")
        
        #name+surname
    if name.isdigit():
        print("yalnisdir")
    elif surname.isdigit():
        print("soyad yalnisdir")
    else:
        print("ad:" + name + " "+"soyad :" + surname)
        
        #nomre serti
    if  phone.isdigit() and  len(phone) == 7:
        print("nomre :"+ "+994"+ phone+" ", end="")
    else:
        print("yalnis nomre", )
        
        #@
    if  "@"in mail:
        print("duzdu")
    else:
        print("@")
        
        
    