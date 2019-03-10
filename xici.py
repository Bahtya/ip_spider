import requests
from pyquery import PyQuery as pq
import time

base_url = 'https://www.xicidaili.com/nn'
headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
}
ip_list = []

def get_list(page):

    url = base_url + "/" + str(page) 
    html = requests.get(url,headers = headers)
    sourxe = pq(html.text)
    items = sourxe('#ip_list tr').items()
    #print(ips)
    for item in items:
        #print(ip.text())
        ip=item('td:nth-child(2)').text()
        port=item('td:nth-child(3)').text()
        address = item('td:nth-child(4)').text()
        tpye = item('td:nth-child(6)').text()
        ping = item('td:nth-child(7) .bar').attr("title")
        dic = {
            "ip":ip,
            "port":port,
            "address":address,
            "type":tpye,
            "ping":ping
        }
        ip_list.append(dic)

if __name__ == "__main__":
    f=open('data.txt','a+')
    for page in range(1,50):
        get_list(page)
        time.sleep(2)
    print(ip_list)
    for ip in ip_list:
        print(ip['ip'])
        if ip['port']==('80' or "8080"):
            f.write(ip['ip']+':'+ip['port']+"\n")
    f.close()


