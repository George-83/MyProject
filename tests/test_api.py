import pytest
import requests
import json
import unittest
import jsonschema
import platform as p


#
# with open("../resources/schemas/people_info_schema.json") as sch:
#     valid_schema = json.load(sch)
#
#
#
#
# @pytest.mark.suite_default
# def test_swapi():
#     response = requests.get("https://swapi.dev/api/people/1/")
#     response_json = response.json()
#     pretty_response = json.dumps(response_json, indent=4)
#     print(pretty_response)
#     print(response_json.__class__)
#     assert response.status_code == 200
#     jsonschema.validate(response_json, valid_schema)
#     sch.close()
#
#
# def test_kcentr_ru():
#     response = requests.get(
#         "https://kcentr.ru/content-service/api/desktop/v1/products?visitorUuid=8485f7ea-f2e7-4478-aff3-e8fe3b0f3cf0&cityUuid=deb1d05a-71ce-40d1-b726-6ba85d70d58f&categoryId=televizory&sortType=price_asc&limit=19")
#     response_json = response.json()
#     response_json_products = response_json["products"]
#     pretty_response_products = json.dumps(response_json_products, indent=4)
#     assert response.status_code == 200
#     print(pretty_response_products)
#     print(response_json_products.__class__)
#     sch.close()
#
#
# def test_open_file():
#     file = open('../resources/schemas/people_info_schema.json')
#     print('\n', type(file), '\n', file.read())
#     file.close()
#
#
# def test_os_name():
#     print('\n', p.uname())
#
#
# class Person:
#     name = "Ivan"
#     age = 29
#
#
# def test_2():
#     vlad = Person()
#     print(Person.age, "\n", Person.name)
#
#
# def test_3(name, age, height):
#     result = name + age + height
#     print(result)
#
#
# def test_5():
#     print(test_3("Igor", "28", "189"))


# Test Suite for website kcentr.ru
# pytest -vm kcenter_api_test tests/test_api.py
@pytest.mark.kcenter_api_test
def test_check_sorting_by_price_asc():
    response = requests.get(
        "https://kcentr.ru/content-service/api/desktop/v1/products?visitorUuid=8485f7ea-f2e7-4478-aff3-e8fe3b0f3cf0&cityUuid=deb1d05a-71ce-40d1-b726-6ba85d70d58f&categoryId=televizory&sortType=price_asc&limit=19")
    response_json = response.json()
    response_products = response_json["products"]
    sorted_by_price = sorted(response_products, key=lambda x: x["price"], reverse=False)
    pretty_response = json.dumps(response_json, indent=4)
    # comparator = response_json["products"][0]["price"]
    # sorted_by_price_pretty = json.dumps(sorted_by_price, indent=4)
    response_products_pretty = json.dumps(response_products, indent=4)
    # print(sorted_by_price.__class__)
    print(response_products.__class__)
    print(pretty_response)
    # assert response.status_code == 200
    assert sorted_by_price == response_products


@pytest.mark.kcenter_api_test
def test_check_filter_by_brand():
    URL = "https://kcentr.ru/content-service/api/desktop/v1/products"
    payload = {
        "visitorUuid": "a2b72613-2852-4df7-81f3-6e9a519453ce",
        "cityUuid": "deb1d05a-71ce-40d1-b726-6ba85d70d58f",
        "categoryId": "televizory",
        "filters[proizvoditel]": "blackton",
        "sortType": "popularity",
        "limit": "19"
    }
    response = requests.get(URL, params=payload)
    response_json = response.json()
    response_products = response_json["products"]
    response_products_pretty = json.dumps(response_products, indent=4)
    print(response_products.__class__)
    print(response_products_pretty)
    assert response.status_code == 200
    for field in response_products:
        assert "Blackton" in field["name"]


@pytest.mark.kcenter_api_test
def test_check_filter_by_brand2():
    URL = "https://kcentr.ru/content-service/api/desktop/v1/products"
    payload = {
        "visitorUuid": "a2b72613-2852-4df7-81f3-6e9a519453ce",
        "cityUuid": "deb1d05a-71ce-40d1-b726-6ba85d70d58f",
        "categoryId": "televizory",
        "filters[proizvoditel]": "panasonic",
        "sortType": "popularity",
        "limit": "19"
    }
    response = requests.get(URL, params=payload)
    response_json = response.json()
    response_products = response_json["products"]
    response_products_pretty = json.dumps(response_products, indent=4)
    print(response_products.__class__)
    print(response_products_pretty)
    assert response.status_code == 200
    for field in response_products:
        assert "Panasonic" in field["name"]


@pytest.mark.kcenter_api_test
def test_check_request_without_callerid():
    URL = "https://kcentr.ru/content-service/api/desktop/v1/products"
    payload = {
        "visitorUuid": "a2b72613-2852-4df7-81f3-6e9a519453ce",
        "cityUuid": "deb1d05a-71ce-40d1-b726-6ba85d70d58f",
        "categoryId": "televizory",
        "sortType": "popularity",
        "limit": "19"
    }
    headers = {
        "cookie": "session_uuid=a2b72613-2852-4df7-81f3-6e9a519453ce; store[region]=deb1d05a-71ce-40d1-b726-6ba85d70d58f; store[city]=%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA; store[region_name]=%D0%A3%D0%B4%D0%BC%D1%83%D1%80%D1%82%D1%81%D0%BA%D0%B0%D1%8F%20%D1%80%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0; KC_CITY_CONFIRMATION_SHOWN=true; _gcl_au=1.1.806095134.1685028644; _ym_uid=1685028644216799538; _ym_d=1685028644; advcake_session_id=deb89821-1afd-1065-9867-cbba9f9c957f; tmr_lvid=bb0ad8a3202a14f5a3ab34fbc169cd7c; tmr_lvidTS=1685028644771; blueID=10d62ec9-5499-4d80-b94c-46a73ef84e87; _ymab_param=7Q71AtUBDjzh2nQNHHUbpxtFyZTT9T65EPpn0h1hmwilptYG-v6Elea0u2FgPH-7XOqZFWxH17xx9N5rHJ-SR6GM5yA; analytic_id=1685028647830301; _acfId=1a55e95f-0057-4eec-9ba9-2e3c99f08418; _userGUID=0:li3ak3je:R8RPJ8wYRg4zdugilse7kvZcaxk0A37I; digi_uc=W1sic3YiLCIxNDQzMjk1IiwxNjg1MDI4NjYxNTQxXV0=; deduplication_cookie=addigital_network; deduplication_cookie=addigital_network; utm_source=addigital_network; utm_medium=cpc; utm_campaign=blueperformance; utm_content=promo; MgidSensorClidV=0; advcake_utm_partner=blueperformance; advcake_utm_webmaster=promo; advcake_click_id=; tt_deduplication_cookie=addigital_network; tt_deduplication_cookie=addigital_network; _gid=GA1.2.1074928972.1685275168; KC_CATALOG_SORT=popularity; _ym_isad=2; advcake_track_id=fd7107d0-d44e-c841-20d4-b6141739495a; advcake_track_url=https%3A%2F%2Fkcentr.ru%2Fgoods%2Ftelevizor_polarline_24pl12tc%2F%3Futm_source%3Daddigital_network%26utm_medium%3Dcpc%26utm_campaign%3Dblueperformance%26utm_content%3Dpromo%26erid%3Dblue0008; _acfVisit=2; MgidSensorNVis=10; MgidSensorHref=https://kcentr.ru/catalog/televizory/proizvoditel=blackton/?sortType=popularity; _ga=GA1.2.120734951.1685028644; tmr_detect=0%7C1685428595187; _ga_VBSF5JSB9F=GS1.1.1685425694.11.1.1685428607.0.0.0"
    }
    response = requests.get(URL, params=payload, headers=headers)
    response_json = response.json()
    response_json_pretty = json.dumps(response_json, indent=4)
    print(response_json.__class__)
    print(response_json_pretty)
    assert response.status_code == 200
