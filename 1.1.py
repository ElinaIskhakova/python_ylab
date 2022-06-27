#Написать метод domain_name, который вернет домен из url адреса:
def domain_name(url):
    url = url.replace('https://', '').replace('http://','').replace('www.','').split('.')[0]
    return url
