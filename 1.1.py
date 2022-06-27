
def domain_name(url):
    return url.replace("www.","http://").split("//")[1].split(".")[0]