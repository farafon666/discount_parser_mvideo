import requests
import json

def get_data():
    import requests

    cookies = {
        '_ym_d': '1649876316',
        '_ym_uid': '164987631664842355',
        'ADRUM': 's=1649876585902&r=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Figrovaya-klaviatura-logitech-g413-tkl-se-920-010447-50170481%3F0',
        '__lhash_': '8f0c9dbc3e1a3c8d78c553b13ebeb4f0',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_984',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20979010353',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '6400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_REGION_ID': '13',
        'MVID_REGION_SHOP': 'S908',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '4',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'authError': '',
        'SMSError': '',
        'tmr_lvid': 'fa28ad6ca03ca230d7c073540f927ad8',
        'tmr_lvidTS': '1649876311444',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '6369d57f-395f-430f-971d-38454515b2e6',
        '_gid': 'GA1.2.1594387380.1656704339',
        'advcake_track_id': 'c91e2f3b-2b22-38d4-d587-3058f4bf7b1d',
        'advcake_session_id': '2b254b4e-5f23-983b-fdde-0aa44e7baee1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_ym_isad': '2',
        'flocktory-uuid': '498f0766-42dc-4e8f-aed5-1a6ec3acce21-0',
        'afUserId': 'c2551424-f541-4962-9293-26550e774d7e-p',
        'AF_SYNC': '1656704339859',
        'mindboxDeviceUUID': 'f052d772-b5f9-4def-a797-1132fe688c0c',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22f052d772-b5f9-4def-a797-1132fe688c0c%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_ga': 'GA1.1.728123470.1656704339',
        'tmr_detect': '0%7C1656704733596',
        'tmr_reqNum': '83',
        'JSESSIONID': 'khKhv1TYX2bfyg1rLbqvJm1YVvCxLdyd1kn2nRLlqXpLdZy02Tmz!870320552',
        'bIPs': '672961728',
        '_ga_CFMZTSS5FM': 'GS1.1.1656704338.1.1.1656704759.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1656704338.1.1.1656704759.31',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_d=1649876316; _ym_uid=164987631664842355; ADRUM=s=1649876585902&r=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Figrovaya-klaviatura-logitech-g413-tkl-se-920-010447-50170481%3F0; __lhash_=8f0c9dbc3e1a3c8d78c553b13ebeb4f0; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_984; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20979010353; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6400000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_REGION_ID=13; MVID_REGION_SHOP=S908; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=4; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; authError=; SMSError=; tmr_lvid=fa28ad6ca03ca230d7c073540f927ad8; tmr_lvidTS=1649876311444; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=6369d57f-395f-430f-971d-38454515b2e6; _gid=GA1.2.1594387380.1656704339; advcake_track_id=c91e2f3b-2b22-38d4-d587-3058f4bf7b1d; advcake_session_id=2b254b4e-5f23-983b-fdde-0aa44e7baee1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_isad=2; flocktory-uuid=498f0766-42dc-4e8f-aed5-1a6ec3acce21-0; afUserId=c2551424-f541-4962-9293-26550e774d7e-p; AF_SYNC=1656704339859; mindboxDeviceUUID=f052d772-b5f9-4def-a797-1132fe688c0c; directCrm-session=%7B%22deviceGuid%22%3A%22f052d772-b5f9-4def-a797-1132fe688c0c%22%7D; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _ga=GA1.1.728123470.1656704339; tmr_detect=0%7C1656704733596; tmr_reqNum=83; JSESSIONID=khKhv1TYX2bfyg1rLbqvJm1YVvCxLdyd1kn2nRLlqXpLdZy02Tmz!870320552; bIPs=672961728; _ga_CFMZTSS5FM=GS1.1.1656704338.1.1.1656704759.0; _ga_BNX5WPP3YK=GS1.1.1656704338.1.1.1656704759.31; MVID_ENVCLOUD=prod1',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/operativnaya-pamyat=12-gb,16-gb,32-gb,8-gb',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-set-application-id': '5102d465-bb04-4159-a72b-5a21fdb078af',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJvcGVyYXRpdm5heWEtcGFteWF0IiwiIiwiMTItZ2IiLCIxNi1nYiIsIjMyLWdiIiwiOC1nYiJd',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w', encoding='utf-8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json', encoding='utf_8') as file:
        products_data = json.load(file)

    with open('4_items_prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()

