import requests
import time


login_url = 'https://xxcapp.xidian.edu.cn/uc/wap/login/check'
url = 'https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save'
username = [,]
password = ['',]
for i in range(len(username)):
    session = requests.session()
    login_data = {
        'username': username[i],
        'password': password[i],
    }
    session.post(url=login_url, data=login_data)
    data = {
        'sfzx': '1',
        'tw': '2',
        'area': '陕西省 西安市 雁塔区',
        'city': '西安市',
        'province': '陕西省',
        'address': '陕西省西安市雁塔区电子城街道二环南路西段西安电子科技大学北校区',
        'geo_api_info': '{"type":"complete","position":{"Q":34.234281955296,"R":108.92003607855997,"lng":108.920036,"lat":34.234282},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":35,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610113","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"太白北路","streetNumber":"334号","country":"中国","province":"陕西省","city":"西安市","district":"雁塔区","towncode":"610113004000","township":"电子城街道"},"formattedAddress":"陕西省西安市雁塔区电子城街道二环南路西段西安电子科技大学北校区","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
        'sfcyglq': '0',
        'sfyzz': '0',
        'qtqk': '',
        'ymtys': '0',
    }
   
    res = session.post(url=url, data=data).json()
    print(username[i], end='--')
    print(time.asctime(time.localtime(time.time())), end='--')
    print(res['m'])


    # 北校区只需将data换为以下数据
    # data = {
    #     'sfzx': '1',
    #     'tw': '2',
    #     'area': '陕西省 西安市 雁塔区',
    #     'city': '西安市',
    #     'province': '陕西省',
    #     'address': '陕西省西安市雁塔区电子城街道二环南路西段西安电子科技大学北校区',
    #     'geo_api_info': '{"type":"complete","position":{"Q":34.234281955296,"R":108.92003607855997,"lng":108.920036,"lat":34.234282},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":35,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610113","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"太白北路","streetNumber":"334号","country":"中国","province":"陕西省","city":"西安市","district":"雁塔区","towncode":"610113004000","township":"电子城街道"},"formattedAddress":"陕西省西安市雁塔区电子城街道二环南路西段西安电子科技大学北校区","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    #     'sfcyglq': '0',
    #     'sfyzz': '0',
    #     'qtqk': '',
    #     'ymtys': '0',
    # }

#  data = {
#         'sfzx': '1',
#         'tw': '1',
#         'area': '陕西省 西安市 长安区',
#         'city': '西安市',
#         'province': '陕西省',
#         'address': '陕西省西安市长安区韦曲街道学而思培优(西长安街校区)',
#         'geo_api_info': '{"type":"complete","position":{"Q":34.158996853299,"R":108.90904676649399,"lng":108.909047,"lat":34.158997},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":8094.548535841807,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610116","businessAreas":[{"name":"韦曲","id":"610116","location":{"Q":34.162202,"R":108.93736899999999,"lng":108.937369,"lat":34.162202}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"西长安街","streetNumber":"599号","country":"中国","province":"陕西省","city":"西安市","district":"长安区","towncode":"610116001000","township":"韦曲街道"},"formattedAddress":"陕西省西安市长安区韦曲街道学而思培优(西长安街校区)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
#         'sfcyglq': '0',
#         'sfyzz': '0',
#         'qtqk': '',
#         'ymtys': '0',
#     }
