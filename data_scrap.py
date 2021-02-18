# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Korea"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'lxml')

"""
HTML Tag분석 (어떻게 데이터를 뽑아올 것인지 구상)
class: barbox tright -> table 태그 -> tbody 태그
<tr> 태그 모두 다 뽑아내기 (리스트)
<tr> 태그 중에서 본격적으로 차트의 데이터가 몇 번째부터 시작이 되는지 확인해서 해당 리스트에 index로 row의 시작 위치 잡기
<tr> 태그가 몇 번째까지가 차트의 데이터인지 확인하기
각 row의 1번째 <td>(Date), 3번째 <td>(# of cases), 네번째 <td>(# of deaths) 값을 각 각의 배열에 담아주기
class="cbs-ibr"(숫자) class="cbs-ibl" (증가추이)
"""
outer_container = soup.find("div", {"class": "barbox tright"})
# barbox tright div tag내부에 있는 table의 모든 tr 태그를 가져온다.
tr = outer_container.find_all('tr')
# tr태그의 끝에서 15번째까지가 해당 테이블에 표시되는 데이터의 영역이므로 slicing
# 끝 ~ 끝에서 17번째 줄 위까지 역순
sliced_tr = tr[-1:-17:-1]
# sliced_tr[15] : 첫번째 행의 데이터 ~ sliced_tr[1] : 가장 마지막 행의 데이터

# 각 행에 총 4개의 <td> 태그로 구성
# 첫 번째 <td> : 날짜
# 세 번째 <td> -> 첫 번째 <span>의 value : # of cases 데이터
# 세 번째 <td> -> 두 번째 <span>의 value : # of cases 증가추이 데이터
# 네 번째 <td> -> 첫 번째 <span>의 value : # of death 데이터
# 네 번째 <td> -> 두 번째 <span>의 value : # of death 증가추이 데이터

"""
입력받은 tr태그로부터 td태그의 데이터를 분리해내는 처리를 하는 메서드
parmas: sliced_tr 
td tag의 사이사이에 "NavigableString"가 있기때문에
1, 3, 4번째 행이 아닌 1, 5, 7번째 행의 데이터를 가져와야 한다.
"""
def extract_td_from_tr(sliced_tr):
    td_list = []
    for tr in list(sliced_tr[-1:-16:-1]):
        td_dict = dict()
        for idx, td in enumerate(tr):
            # date
            if idx == 1:
                td_dict['date'] = td.text
            # cases
            if idx == 5:
                td_dict['cases'] = td.text
            # death
            if idx == 7:
                td_dict['death'] = td.text
        td_list.append(td_dict)
    return td_list


"""
최종적으로 정렬된 리스트 데이터를 반환하는 메서드
"""
def get_extracted_data():
    return extract_td_from_tr(sliced_tr)
