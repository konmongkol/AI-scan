import bs4
import requests

i = 30000000

while True:
    i = i + 1 
    try:
        data = requests.get('https://pantip.com/topic/'+str(i))
        soup = bs4.BeautifulSoup(data.text)
        s = soup.find('div',{'class':'content'})
        s1 = s.find('div',{'class':'container-outer container-liquid'})
        s2 = s1.find('div',{'class':'container-inner'})
        s3 = s2.find('div',{'class':'display-post-wrapper main-post type'})
        # s4 = soup.find("h4",{"style":"font-weight: bold;"})
        s4 = s3.find('div',{'class':'main-post-inner sticky-navi-comment'})
        s5 = s4.find('div',{'class':'display-post-status-leftside'})
        s5 = soup.find("h2",{"class":"display-post-title"})
        # print(s5.text)
    # print(i,str(s5.text))
    # print(s4.text)
        f = open("pantip_save.txt", "a",encoding='utf-8')
        f.write(s5.text+"\n")
        f.close()
    
    # print(s4.text)
    
        
        
    except:
        print(i)
        pass
        