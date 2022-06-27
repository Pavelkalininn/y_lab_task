def domain_name(url):
    splitted_www = url.split('www.')
    if len(splitted_www) > 1:
        return splitted_www[1].split('.')[0]
    return url.split('//')[1].split('.')[0]


if __name__ == "__main__":
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
