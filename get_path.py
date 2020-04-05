import requests
import datetime
from pyquery import PyQuery as pq

url = "https://cdn.pamyat-naroda.ru/data/CiS7ta8gzdGMQtiPNrEY3g/1586077193/pamyat/map_army_unit_label/_search"

headers = {
    'origin': 'https://pamyat-naroda.ru',
    'referer': 'https://pamyat-naroda.ru/warunit/402%20%D1%81%D0%BF/?backurl=/warunit/?q%3D402%20%D1%81%D0%BF%26page%3D1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}    

data1 = '{\"query\":{\"bool\":{\"must\":[{\"match_phrase\":{\"division_name\":{\"query\":\"'
data2 = '\"}}}]}},\"_source\":[\"image_path\",\"date_from\",\"date_to\",\"id\",\"division_name\",\"shirota\",\"dolgota\",\"image_path\",\"map_id\",\"location\"],\"sort\":{\"id\":\"asc\"},\"size\":10000}'


def get_path(army_name):
    
    data = data1 + army_name + data2
    data = data.encode('utf-8')
    
    res = requests.post(url, data=data, headers=headers)
    res.json()
    
    res = res.json()
    res = res['hits']
    
    #npoints = res['total']
    result = res['hits']
    
    valid_info = {}
    
    dates = [] 
    
    for i in result:
        if i['_source']['date_from'] != None:
            dates.append(i['_source']['date_from'])

    sdates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in dates]
    sdates.sort()

    sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in sdates]
        
    
    valid_info = {}

    k = 0
    for i in sorteddates:
        for j in result:
            if j['_source']['date_from'] == i:
                dolgota = {'dolgota': j['_source']['dolgota']}
                shirota = {'shirota': j['_source']['shirota']}
                date_from = {'date_from': j['_source']['date_from']}
                date_to = {'date_to': j['_source']['date_to']}
                tmp = [dolgota, shirota, date_from, date_to]
                valid_info['point' + str(k)] = tmp
                k += 1
                break
            
    '''
        Функция возвращает словарь с координатными точками, отсортированными по дате.
    '''
                
    return valid_info


if __name__ == "__main__":
    print(get_path('123 тбр'))
