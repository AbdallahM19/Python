print ("Hello Mohamed")

Email = str(input(" inter your email : "))
Start = Email.find("@") + 1
End = len ( Email )
print (Email [ Start : End ] )