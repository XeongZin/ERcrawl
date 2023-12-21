import bs4
from bs4 import BeautifulSoup 
import urllib.request
import json
import datetime

from datetime import datetime
import pytz

# 한국 시간대 설정
korea_timezone = pytz.timezone('Asia/Seoul')

# 현재 시간을 UTC로 가져오기
utc_now = datetime.utcnow()

# UTC 시간을 한국 시간대로 변경
korea_now = utc_now.replace(tzinfo=pytz.utc).astimezone(korea_timezone)
korea_now_time = korea_now.strftime('%Y년 %m월 %d일 %H시 %M분')

print("\n Exchange Rate Webcrawling Project")
print('환영합니다. ' + korea_now_time)
print('주요 나라 12개국의 환율 정보를 요약해 드리겠습니다.\n')

def scrape_ER():
    #request를 통해 웹 페이지 전체의 소스 코드를 가져옴
    #미국 환율
    url1 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EB%AF%B8%EA%B5%AD%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url1, "html.parser")
    unit1 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    usdnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    usdgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 미국 환율 :', unit1, '당', usdnow, '원, 전일대비 : ', usdgap)

    #일본 환율
    url2 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EC%9D%BC%EB%B3%B8%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url2, "html.parser")
    unit2 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    jpynow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    jpygap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 일본 환율 :', unit2, '당', jpynow, '원, 전일대비 : ', jpygap)

    #유럽 연합 환율
    url3 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EC%9C%A0%EB%9F%BD%EC%97%B0%ED%95%A9%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url3, "html.parser")
    unit3 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    eurnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    eurgap = soup.find('span', attrs={'class':'price_gap'}).get_text()  # 상승 폭
    print('--> 유럽 연합 환율 :', unit3, '당', eurnow, '원, 전일대비 : ', eurgap)

    #중국 환율
    url4 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EC%A4%91%EA%B5%AD%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url4, "html.parser")
    unit4 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    cnynow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    cnygap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 중국 환율 :', unit4, '당', cnynow, '원, 전일대비 : ', cnygap)
    
    #영국 환율
    url5 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EC%98%81%EA%B5%AD%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url5, "html.parser")
    unit5 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    gbpnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    gbpgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 영국 환율 :', unit5, '당', gbpnow, '원, 전일대비 : ', gbpgap)

    #호주 환율
    url6 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%ED%98%B8%EC%A3%BC%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url6, "html.parser")
    unit6 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    audnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    audgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 호주 환율 :', unit6, '당', audnow, '원, 전일대비 : ', audgap)

    #캐나다 환율
    url7 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EC%BA%90%EB%82%98%EB%8B%A4%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url7, "html.parser")
    unit7 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    cadnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    cadgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 캐나다 환율 :', unit7, '당', cadnow, '원, 전일대비 : ', cadgap)

    #뉴질랜드 환율
    url8 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EB%89%B4%EC%A7%88%EB%9E%9C%EB%93%9C%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url8, "html.parser")
    unit8 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    nzdnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') # 환율 표시
    nzdgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 뉴질랜드 환율 :', unit8, '당', nzdnow, '원, 전일대비 : ', nzdgap)

    #태국 환율
    url9 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%ED%83%9C%EA%B5%AD%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url9, "html.parser")
    unit9 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() # 단위
    thbnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') #환율 표시
    thbgap = soup.find('span', attrs={'class':'price_gap'}).get_text() # 상승 폭
    print('--> 태국 환율 :', unit9, '당', thbnow, '원, 전일대비 : ', thbgap)

    #베트남 환율
    url10 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EB%B2%A0%ED%8A%B8%EB%82%A8%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url10, "html.parser")
    unit10 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() #단위
    vndnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') #환율 표시
    vndgap = soup.find('span', attrs={'class':'price_gap'}).get_text() #상승 폭
    print('--> 베트남 환율 :', unit10, '당', vndnow, '원, 전일대비 : ', vndgap)

    #홍콩 환율
    url11 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%ED%99%8D%EC%BD%A9%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url11, "html.parser")
    unit11 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() #단위
    hkdnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') #환율 표시
    hkdgap = soup.find('span', attrs={'class':'price_gap'}).get_text() #상승 폭
    print('--> 홍콩 환율 :', unit11, '당', hkdnow, '원, 전일대비 : ', hkdgap)

    #대만 환율
    url12 = urllib.request.urlopen('https://search.naver.com/search.naver?sm=mtb_drt&where=m&query=%EB%8C%80%EB%A7%8C%ED%99%98%EC%9C%A8')
    soup = BeautifulSoup(url12, "html.parser")
    unit12 = soup.find('span', attrs={'class':'nb_txt _pronunciation'}).get_text() #단위
    twdnow = soup.find('strong', attrs={'class':'price'}).get_text().replace('현재 환율','') #환율 표시
    twdgap = soup.find('span', attrs={'class':'price_gap'}).get_text() #상승 폭
    print('--> 대만 환율 :', unit12, '당', twdnow, '원, 전일대비 : ', twdgap)

    exchange_rate = []
    try:
        exchange_rate.append(unit1)
        exchange_rate.append(usdnow)
        exchange_rate.append(usdgap)

        exchange_rate.append(unit2)
        exchange_rate.append(jpynow)
        exchange_rate.append(jpygap)

        exchange_rate.append(unit3)
        exchange_rate.append(eurnow)
        exchange_rate.append(eurgap)

        exchange_rate.append(unit4)
        exchange_rate.append(cnynow)
        exchange_rate.append(cnygap)

        exchange_rate.append(unit5)
        exchange_rate.append(gbpnow)
        exchange_rate.append(gbpgap)

        exchange_rate.append(unit6)
        exchange_rate.append(audnow)
        exchange_rate.append(audgap)

        exchange_rate.append(unit7)
        exchange_rate.append(cadnow)
        exchange_rate.append(cadgap)

        exchange_rate.append(unit8)
        exchange_rate.append(nzdnow)
        exchange_rate.append(nzdgap)

        exchange_rate.append(unit9)
        exchange_rate.append(thbnow)
        exchange_rate.append(thbgap)

        exchange_rate.append(unit10)
        exchange_rate.append(vndnow)
        exchange_rate.append(vndgap)

        exchange_rate.append(unit11)
        exchange_rate.append(hkdnow)
        exchange_rate.append(hkdgap)

        exchange_rate.append(unit12)
        exchange_rate.append(twdnow)
        exchange_rate.append(twdgap)
    except IndexError:
        pass
    return exchange_rate

    
if __name__ == "__main__":
    scrape_ER()