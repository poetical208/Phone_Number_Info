import phonenumbers
import os
from plyer import notification
from phonenumbers import geocoder
from phonenumbers import carrier
while True:
    os.system("cls")
    a = input("Please Enter Your Phone No.[XXXXXXXXXX]: ")
    if len(a) == 10 and a.isdigit():
        try:
            b = phonenumbers.parse("+91"+a)
            x = carrier.name_for_number(b, 'en')
            if geocoder.description_for_number(b, 'en') == "" or carrier.name_for_number(b, 'en') == "":
                notification.notify(title="Phone Number Info by: Satyam Tripathi",
                                    message="\n\tAlert! Number is Invalid, Please Try Again",
                                    app_icon="C:/Users"
                                             "/Dell/Downloads/err.ico", timeout=7)
            else:
                notification.notify(title="Phone Number Info by: Satyam Tripathi",
                                    message=f"\n\t  Your Phone Number : {a[:]}"
                                    f"\n\t  Your Country: {geocoder.description_for_number(b, 'en').upper()}\n\t  SIM"
                                    f" Card: {carrier.name_for_number(b, 'en').title()}",
                                    app_icon="C:/Users"
                                             "/Dell/Downloads/sim.ico", timeout=7)

        except:
            notification.notify(title="Phone Number Info by: Satyam Tripathi",
                                message="\n\tAlert! Number is Invalid, Please Try Again",
                                app_icon="C:/Users"
                                         "/Dell/Downloads/err.ico", timeout=7)

    else:
        notification.notify(title="Phone Number Info by: Satyam Tripathi",
                            message="\n\tAlert! Number is Invalid, Please Try Again",
                            app_icon="C:/Users"
                                     "/Dell/Downloads/err.ico", timeout=7)
