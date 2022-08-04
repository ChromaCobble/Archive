#Ata Anıl Altıntaş
#9/E
#Yönetici ve Çalışan için kullanıcı arayüzü olan, kalıcıdosya depolama sistemi olan bir Depo - malzeme yönetim programıdır.
#Program ilk önce kendi dosya sistemi yok ise bulunduğu dizine oluşturur, daha sonra bu dizini kullanıcı isteği doğrultusunda şekillendirir ve lazım olduğunda bilgi almak için kullanır.

#Libraries
import time
import os
import datetime


#startup
name = "E-Management"
version = "1.0_Beta"


if os.path.exists("data"):
    pass
else:
    os.makedirs("data")
if os.path.exists("data//storage"):
    pass
else:
    os.makedirs("data//storage")

if os.path.exists("data//log"):
    pass
else:
    os.makedirs("data//log")

if os.path.exists("data//ban"):
    pass
else:
    os.makedirs("data//ban")
    
if os.path.exists("data//employee"):
    pass
else:
    os.makedirs("data//employee")
    
if os.path.exists("data//admin"):
    pass
else:
    os.makedirs("data//admin")
if os.path.exists("data//employee//idcount.data"):
    pass
else:
    f = open("data//employee//idcount.data","w")
    f.write("000")
    f.close()
if os.path.exists("data//admin//idcount.data"):
    pass
else:
    f = open("data//admin//idcount.data","w")
    f.write("000")
    f.close()
    



#defines

    
def table(n):
    print("_"*n)
def space():
    print("""
    """ *40)
    
    

def login(state):
    if state == "yonetici":
        space()
        table(15)
        print("Lütfen yönetici giriş şifrenizi giriniz.")
        y_continue == int(input(">>"))
        
        
        
#start   
while True:
    space()
    table(15)
    

    print("Sisteme kayıt[1]")
    print("Sisteme giriş[2]")
    print("Yardım[3]")
    table(10)
    c = int(input(">>"))

    if c == 2:
        print("Yönetici giriş[1]")
        print("Çalışan giriş[2]")
        g = int(input(">>"))
        if g == 2:
            space()
            
            table(12)
            print("Lütfen giriş yapınız.(Giriş sistemi büyük küçük harfler ve özel karakterlere duyarlıdır.)")
            table(5)
            l_name = input("İsminiz :")
            s_name = input("Soyisminiz :")
            continuew = input("Sistem şifreniz :")
            b_direct = "data//ban"+l_name+"-"+s_name+".data"
            if os.path.exists(b_direct):
                f = open(b_direct,"r")
                line = f.read().splitlines()
                
                print("Çalışan hesabınıza",line[0],"tarihinde engel koyulmuştur.")
                input()
                break
                
            direct = "data//employee//"+l_name+"-"+s_name+".data"
            if os.path.exists(direct):
                f = open(direct,"r")
                lines = temp = f.read().splitlines()
                continuetest = lines[2]
                f.close()
                if continuew == continuetest:
                    #gather information part in the login section
                    f = open(direct,"r")
                    name = f.readline()
                    s_name = f.readline()
                    f.readline() #continueword
                    r_date = f.readline()
                    f.close()
                    space()
                    table(20)
                    print("Hoşgeldiniz,")
                    print(name,s_name,"!")
                    table(20)
                ###############
                    table(10)
                    print("Depoya ürün ekle[1]")
                    print("Depodan ürün çıkar[2]")
                    print("Depolar ve ürün bilgilerini görüntüle[3]")
                    z = int(input(">>"))
                    if z == 1:
                        if os.listdir("data//storage") == []:
                            print("Hiçbir depo bulunmamaktadır, lütfen bir depo ekleyiniz.")
                            continue
                        else:
                            print(os.listdir("data//storage"))
                            table(10)
                            print("Lütfen bir depo seçin.")
                            dep = input(">>")
                            
                            
                            table(10)
                            print("Lütfen malzeme kriterlerini giriniz.")
                            n_item = input("Malzeme ismi :")
                            c_item = input("Malzeme adeti :")
                            a_item = input("Ek notlar (Yoksa boş bırakın) :")
                            direct = "data//storage//"+dep+"//"+n_item+".data"
                            f = (direct,"w")
                            f.write(n_item)
                            f.write("\n")
                            f.write(c_item)
                            f.write("\n")
                            f.write(a_item)
                            f.write("\n")
                            f.write(a_item)
                            f.write("\n")
                            f.write(datetime.datetime.now().strftime ("%Y-%m-%d"))
                            
                            f.close()
                            print("Malzemeniz başarılı şekilde",dep,"deposuna kayıt edildi!")
                            continue 

                    elif z == 2:
                         print(os.listdir("data//storage"))
                         table(10)
                         print("Lütfen bir depo seçin.")
                         dep = input(">>")
                            
                            
                         table(10)
                         print("Lütfen malzeme kriterlerini giriniz.")
                         n_item = input("Malzeme ismi :")
                         direct = "data//storage//"+dep+"//"+n_item+".data"
                         os.remove(direct)
                            
                           
                         print("Malzemeniz başarılı şekilde",dep,"deposundan silindi!")
                         continue 
                    elif z == 3:
                        print(os.listdir("data//storage"))
                        table(19)
                        print("Ürün bilgisi alacağınız depoyu seçiniz :")
                        dep = input(">>")
                        direct = "data//storage//"+dep
                        table(19)
                        print(os.listdir("data//storage//"+dep))
                        print("Ürününüzü seçiniz :")
                        n_item = input(">>")
                        direct = "data//storage//"+dep+"//"+n_item+".data"
                        f = open(direct,"r")
                        lines = f.readlines()
                        f.close()
                        table(20)
                        print("\t Ürünün bulunduğu deponun ismi :",dep)
                        print("\t Ürün ismi :",lines[0])
                        print("\t Ürün adeti :",lines[1])
                        print("\t Ürün ile alakalı ek notlar :",lines[2])
                        print("\t Ürün eklenme tarini :",lines[3])
                        table(20)
                        input()
                        continue
                    else:
                        print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                        input()
                        continue

                else:
                    print("Hesabınızın şifresi hatalıdır, lütfen tekrar deneyiniz!")
                    input()
                     
        
                    

                    
                        
                


                    
                
                    
            else:
                print("Kayıtta bulunamamaktısınız, lütfen tekrar deneyiniz ve girdiğiniz bilgileri kontrol ediniz.")
                input()
                    
           
        if g == 1:
            space()
            table(12)
            print("Lütfen giriş yapınız.(Giriş sistemi büyük küçük harfler ve özel karakterlere duyarlıdır.)")
            table(5)
            l_name = input("İsminiz :")
            s_name = input("Soyisminiz :")
            continuew = input("Sistem şifreniz :")
            direct = "data//admin//"+l_name+"-"+s_name+".data"
            b_direct = "data//ban"+l_name+"-"+s_name+".data"
            if os.path.exists(b_direct):
                f = open(b_direct,"r")
                line = f.read().splitlines()
                f.close()
                
                print("Yönetici hesabınıza",line[0],"tarihinde engel koyulmuştur.")
                input()
                break
            if os.path.exists(direct):
                
                f = open(direct,"r")
                lines = f.read().splitlines()
                continuetest = lines[2]
                f.close()
                if continuew == continuetest:
                    while True:
                        #gather information part in the login section
                        f = open(direct,"r")
                        name = f.readline()
                        s_name = f.readline()
                        f.readline() #continueword
                        r_date = f.readline()
                        f.close()
                        space()
                        table(20)
                        print("Hoşgeldiniz,")
                        print("Sayın",name,s_name,"!")
                        table(20)
                        ##############
                        table(10)
                        print("DEPO KOMUTLARI")
                        table(5)
                        print("Depoya ürün ekle[1]")
                        print("Depodan ürün çıkar[2]")
                        print("Depo ekle[3]")
                        print("Depolar ve ürün bilgilerini görüntüle[4]")
                        table(5)
                        print("ÇALIŞAN YÖNETİMİ")
                        table(5)
                        print("Komut geçmişlerini kontrol et[Yakın zamanda mevcut olacaktır.]")
                
                        print("Kişi çıkar[5]")
                        print("Kişi engelle[6]")
                        print("Kişi engeli kaldır[7]")
                        print("Kişi bilgileri ve ekli kişiler[8]")
                        table(5)
                        table(10)
                        z = int(input(">>"))
                        if z == 1:
                            if os.listdir("data//storage") == []:
                                print("Hiçbir depo bulunmamaktadır, lütfen bir depo ekleyiniz.")
                                continue
                            else:
                                print(os.listdir("data//storage"))
                                table(10)
                                print("Lütfen bir depo seçin.")
                                dep = input(">>")
                                
                                
                                table(10)
                                print("Lütfen malzeme kriterlerini giriniz.")
                                n_item = input("Malzeme ismi :")
                                c_item = input("Malzeme adeti :")
                                a_item = input("Ek notlar (Yoksa boş bırakın) :")
                                direct = "data//storage//"+dep+"//"+n_item+".data"
                                f = open(direct,"w")
                                f.write(n_item)
                                f.write("\n")
                                f.write(c_item)
                                f.write("\n")
                                f.write(a_item)
                                f.write("\n")
                                f.write(a_item)
                                f.write("\n")
                                f.write(datetime.datetime.now().strftime ("%Y-%m-%d"))
                                
                                f.close()
                                print("Malzemeniz başarılı şekilde",dep,"deposuna kayıt edildi!")
                                continue 
                            
                        elif z == 2:
                            if os.listdir("data//storage") == []:
                                print("Hiçbir depo bulunmamaktadır.")
                                continue
                            else:
                                print(os.listdir("data//storage"))
                                table(10)
                                print("Lütfen bir depo seçin.")
                                dep = input(">>")
                                
                                
                                table(10)
                                print("Lütfen malzeme kriterlerini giriniz.")
                                n_item = input("Malzeme ismi :")
                                direct = "data//storage//"+dep+"//"+n_item+".data"
                                os.remove(direct)
                                
                               
                                print("Malzemeniz başarılı şekilde",dep,"deposundan silindi!")
                                continue 
    
                            
                            
                        elif z == 3:
                            space()
                            table(10)
                            print("Lütfen ekleyeceğiniz deponun ismini giriniz.")
                            dep = input(">>")
                            print(dep,"adlı depoyu eklemek istediğinizden emin misiniz? (e/h)")
                            h = input(">>")
                            if h == "e" or "E":
                                direct = "data//storage//"+dep
                                os.mkdir(direct)
                                print("Başaralı bir şekilde",dep,"adlı depo eklendi!")
                        
    
                        elif z == 4:
                            space()
                            print(os.listdir("data//storage"))
                            table(19)
                            print("Ürün bilgisi alacağınız depoyu seçiniz :")
                            dep = input(">>")
                            direct = "data//storage//"+dep
                            table(19)
                            print(os.listdir("data//storage//"+dep))
                            print("Ürününüzü seçiniz :")
                            n_item = input(">>")
                            direct = "data//storage//"+dep+"//"+n_item+".data"
                            f = open(direct,"r")
                            lines = f.readlines()
                            f.close()
                            table(20)
                            print("\t Ürünün bulunduğu deponun ismi :",dep)
                            print("\t Ürün ismi :",lines[0])
                            print("\t Ürün adeti :",lines[1])
                            print("\t Ürün ile alakalı ek notlar :",lines[2])
                            print("\t Ürün eklenme tarini :",lines[3])
                            table(20)
                            input()
                            continue
                            
    
                        
                        elif z == 5:
                            space()
                            print("Çıkaracağınız kişinin bilgilerini girin :")
                            state = input("Yönetici/Çalışan :")
                            if state == "yönetici" or "Yönetici":
                                state = "admin"
                            elif state == "Çalışan" or "çalışan":
                                state = "employee"
                            else:
                                print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                                input()
                                continue
                            l_isim = input(state," ismi :")
                            s_isim = input(state," ismi :")
                            table(10)
                            print("Bu kişiyi çıkarmak istediğinizden emin misiniz? (e/h)")
                            h = input(">>")
                        
                            if h == "e" or "E":
                                direct = "data//"+state+"//"+l_isim+"-"+s_isim+".data"
                                os.remove(direct)
                                print(l_isim,s_isim,"adlı çalışan başarılı bir şekilde kaldırıldı!")
                                input()
                                continue
                            elif h == "h" or "H":
                                continue
                            else:
                                print("Hatalı seçim")
                                continue
                            
                            
    
                        
    
                        elif z == 6:
                            space()
                            table(10)
                            print("Lütfen engelleyeceğiniz çalışan veya yöneticinin bilgilerini girin.")
                            l_isim = input("İsim :")
                            s_isim = input("Soyad :")
                            table(5)
                            print("Bu kişiyi engellemek istediğinizden emin misiniz? (e/h)")
                            ab = input(">>")
                            if ab == "e" or "E":
                                direct = "data//ban"+l_isim+"-"+s_isim+".data"
                                f = open(direct,"w")
                                f.write(datetime.datetime.now().strftime ("%Y-%m-%d"))
                                f.close()
                                print(l_isim,s_isim,"adlı kişi başarılı bir şekilde engellendi.")
                            else:
                                continue
                                
                        elif z == 7:
                            space()
                            table(10)
                            print("Lütfen engelini kaldıracağınız çalışan veya yöneticinin bilgilerini girin.")
                            l_isim = input("İsim :")
                            s_isim = input("Soyad :")
                            table(5)
                            print("Bu kişinin engelini kaldırmak istediğinizden emin misiniz? (e/h)")
                            ab = input(">>")
                            if ab == "e" or "E":
                                direct = "data//ban//"+l_isim+"-"+s_isim+".data"
                                os.remove(direct)
                                print(l_isim,s_isim,",adlı kişinin başarılı bir şekilde engeli kaldırıldı.")
                                
                            else:
                                continue
                            
                        elif z == 8:
                            space()
                            table(10)
                            print("Ekli olan çalışanlar")
                            
                            print(os.listdir("data//employee//"))
                            table(10)
                            table(10)
                            print("Ekli olan yöneticiler")
                            print(os.listdir("data//admin//"))
                            table(10)
                            print("Hakkında bilgi almak istediğiniz bir kullanıcı  bilgilerini giriniz : ")
    
                            state = input("Yönetici / Çalışan :")
                        
                            if state == "yönetici" or "Yönetici":
                                state = "admin"
                            elif state == "Çalışan" or "çalışan":
                                state = "employee"
                            else:
                                break
    
                            name = input("ismi :")
                            s_name = input("soyadı :")
                            direct = "data//"+state+"//"+name+"-"+s_name+".data"
                            if not os.path.exists(direct):
                                print("Girdiğiniz kriterlerdeki kullanıcı bulunamadı!")
                                continue
                            else:
                                f = open(direct,"r")
                                lines = f.readlines()
                                table(15)
                                print(state," adı :",lines[0])
                                print(state,"soyadı :",lines[1])
                                if state == "admin":
                                    continue
                                else:
                                    print(state," şifresi :",lines[2])
                                    print(state,"kayıt tarihi :",lines[3])
                                input
                                continue
                                
    
                        else:
                            print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                            input()
                            continue
                        

                    else:
                        print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                        input()
                        continue
                    



            
 

        
    if c == 1:
        space()
        table(15)
        
        print("Yönetici kayıt[1]")
        print("Çalışan kayıt[2]")
        table(15)
        d = int(input(">>"))
        if d == 2:
            space()
        
          
    
            table(10)
            print("Lütfen kayıt edeceğiniz kişinin aşağıdaki formunu doldurunuz.")
            c_id = 0
            c_isim = input("Çalışanın ismi: ")
            c_soy  = input("Çalışanın soyadı: ")
            direct = "data//employee//"+c_isim+"-"+c_soy+".data"
            if os.path.exists(direct):
                print("lütfen farklı bir kullanıcı ismi giriniz!")
            b_direct = "data//ban//"+c_isim+"-"+c_soy+".data"
            if os.path.exists(b_direct):
                f = open(b_direct,"r")
                line = f.read().splitlines()
                
                print("Üzgünüz, bu hesaba",line[0],"tarihinde engel koyulmuştur.")
                input()
                break
            c_continue = input("Çalışanın login şifresi: ")
            print("Bu kayıt formunun kayıt edilmesini istiyor musunuz? (e/h)")
            e = input(">>")
            if e == "e" or "E":
            
                table(10)
            
                print(c_isim," ",c_soy,"adlı çalışanınız kayıt ediliyor, lütfen bekleyiniz..")
                f = open("data//employee//idcount.data","r+")
                e_id = int(f.read())
                e_id += 1
                f.close()
                os.remove("data//employee//idcount.data")
                f = open("data//employee//idcount.data","w")
                f.write("\n")
                f.write(str(e_id))
                f.close()
                direct = "data//employee//"+c_isim+"-"+c_soy+".data"
                fe = open(direct,"w")
                fe.write(c_isim)
                fe.write("\n")
                fe.write(c_soy)
    
                fe.write("\n")
                fe.write(c_continue)
    
                fe.write("\n")
                fe.write(str(e_id))
        
        
                fe.write(datetime.datetime.now().strftime ("%Y-%m-%d"))
                fe.close()
                continue
            else:
                print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                input()
                continue
    
        if d == 1:
            space()
            table(10)
            print("Lütfen admin giriş bilgilerinizi doldurunuz.")
            y_id = 0
            y_isim = input("İsminiz: ")
            y_soy  = input("Soyadınız: ")
            b_direct = "data//ban//"+y_isim+"-"+y_soy+".data"
            if os.path.exists(b_direct):
                f = open(b_direct,"r")
                line = f.read().splitlines()
                f.close()
                print("Üzgünüz, bu hesaba",line[0],"tarihinde engel koyulmuştur.")
                input()
                break
            y_continue = input("Login şifreniz: ")
            print("Bu kayıt formunun kayıt edilmesini istiyor musunuz? (e/h)")
            c = input(">>")
            if c == "e" or "E":
            
                table(10)
            
                print(y_isim," ",y_soy,",sisteme kayıtınız gerçekleştiriliyor, lütfen bekleyiniz..")
                f = open("data//admin//idcount.data","r+")
            
                e_id = int(f.read())
            
                e_id += 1
                f.close()
                os.remove("data//admin//idcount.data")
                f = open("data//admin//idcount.data","w")
                f.write("\n")
                f.write(str(e_id))
                f.close()
                direct = "data//admin//"+y_isim+"-"+y_soy+".data"
                fe = open(direct,"w")
                fe.write(y_isim)
                fe.write("\n")
                fe.write(y_soy)
    
                fe.write("\n")
                fe.write(y_continue)
    
                fe.write("\n")
                fe.write(str(e_id))
            
            
                fe.write(datetime.datetime.now().strftime ("%Y-%m-%d"))
                fe.close()
                continue

            else:
                print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
                input()
                continue
                
           
    if c == 3:
        table(50)
        print(name,version,"sürümüne hoşgeldiniz! Bu program, Burak Bora Anadolu Lisesi 9/E sınıfından Ata Anıl Altıntaş tarafından python dilinde kodlanmıştır. Bu program, bir çalışan yönetim sistemidir.")
        table(50)
        print("Seçimlerinizin yanındaki [ ] sayılarını girip ENTER tuşuna basarak sistem içinde hareket edebilirsiniz.")
        table(40)
        print("Bu program geliştirilme aşamasındadır ve herhangi bir hata olursa lütfen ataaniln@yandex.com adresinden bana ulaşın")
        input()
        continue
    
    

    else:
        print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
        input()
        continue
else:
    print("Yanlış veya hatalı bir seçim yaptınız, lütfen tekrar deneyiniz!")
    input()
    cntinue
        
        
