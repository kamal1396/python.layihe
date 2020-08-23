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


for i in range(0,1):
    kod = int(input("kodu daxil edin: "))
    name = input("ad yazin :")
    surname = input("soyad yazin :")
    mail =  input("mail daxil edin: ")
    phone = input("nomre daxil edin: ")
    telebe= student(kod,name,surname,mail,phone)
    arr.append(telebe)
    print(arr[0].showinfo(kod,name,surname,mail,phone))
    
if kod<1000 & kod>=100:
    print("duzdu")
else:
    print("sevdi")