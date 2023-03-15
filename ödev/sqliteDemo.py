import sqlite3

def listele():
    baglanti = sqlite3.connect("chinook/chinook.db") # veri tabanına baglanılır.
    cursor = baglanti.execute("select FirstName,LastName from customers") # ec çalıştır sorgutu çalıştır
    
    
    for satir in cursor:  # cursor her satırında dolaş
        print(satir[1]) # birinci sutun yazdır
    
    baglanti.close()  # kapat
    
listele()

#Dark Tranqulity -Lethe