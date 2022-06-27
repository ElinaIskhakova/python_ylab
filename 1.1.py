#Написать метод domain_name, который вернет домен из url адреса:
def domain_name(url):
    return url.replace("www.","http://").split("//")[1].split(".")[0]
