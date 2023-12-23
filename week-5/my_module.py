# # import pandas as pd # top level code

# # df = pd.DataFrame([1, 2]) # top level code

# # print("This is my module") # top level code
# # print(__name__)
# # print(pd.__name__)

# import datetime
# from datetime import timezone # datetime dosyasından timezone fonksiyonunu import ettik
# print(timezone.__name__)
# print(datetime.__name__)

def my_function():
    print("Hello")

def call_api(request):
    pass

# my_function() # Fonksiyonu çağırdık, başka bir dosyada çağırmak için import etmemiz gerekir.

if __name__ == "__main__": # Eğer kod bloğunda name in karşılığında main'e eşitse, fonksiyonu çalıştır.
    my_function()
    request = ""
    call_api(request)

# Bu modulde çalıştırmak yerine fonksiyonları tanımladıktan sonra başka bir dosyada import edip bu fonksiyonları da çağırabiliriz.


