import pytest
import requests
import json
import jsonschema
import platform as p

with open("../Resources/Schemas/people_info_schema.json") as sch:
    valid_schema = json.load(sch)

cookies = {
    'ai_user': 'mY2zYC6DInPCnQM/5ZugtE|2023-04-03T12:04:00.182Z; AppServiceAuthSession=h23Navck/7SeyM93VTA6d+TL7fygS7YtBM2ClxEJFio9Lr7qx2yu3KllGNM99mYuBgAYMPVn8zVpj+XyJpI6JtvIOKks3n7y/mMAmm23Z2l2Ag+/1xVqTriDosSgo6kXK3IAwtpHmtBJzw0Tj7vugtwhujLnSdufFrMLhF45T2LxDwootGjtsqFzExlpSKwioY5S8Od1ikEctjFDNKAOnoIyCKTp12d276CdCew+O5uhED0DSjVvJegv0GOFev1785W/sZkuiiMYV4l3lXPLmBtX/sF19UiVK7r+SUFWz+3wH8Rt8uA817tDzW8U+THefKnKa2+KwBIhYkhs89PfaZZLVI9OyUg5OsMr4UHQIyavucUVAiZaSyxKUwca5cxadCJEormRV33yD4yAVdJc9PTYlX7n+xvKJoeWNWhaMktSYwRGcUo5tpZQjlH6hMhcOrMNuj014H1Wg9WZPvu8WdsE5KeErsj7Dz6p57ibNKsTA5oYaOL5nMPWkhBhVQ4RTx+2CS4FTdoLkiqKqfrbNdkeaqk5n1gs8DL08PbwEyje/99+G5F4bWU6ljXJYVRH42DaLOjMs9/vzN6scmaVLN5oXiGEcAbZ9F0JTQGYnEVkwS11Qc64/XkyljPtyRAT/c8MCRsHtgRcm1h2fK52JNSioxRCVT8jwPDHrulvI8PGEwnyXvgdhWF+T3CDug2VB29F03tpc7+OgOt4m2jPspqnzCalAlFZY+dXkvsDKkM9QHYBiIiCL8MOa3oIc0BThfn+2muvVzhdcRoWEsw8nFd1yHDf/DSmDIYcMJZpxH3vh0IGAb7zdmSEn4Ak3veOxohL0lyG6tRZPwEg/KPAF/oO+4/XagOrFuz6U0vHhmg=; ai_session=0T1SE0503BriokS/S08K99|1683029918169|1683029988501'}
callerid = {'callerid': 'customerPortalCaller'}


def test_can_call_endpoint():
    url = "https://pay.test.bcdtravel.com/portal/statements?page=1&orderBy=Date%20To&orderDirection=DESC"
    response = requests.get(url, cookies=cookies, headers=callerid)
    response_json = response.json()
    pretty_response = json.dumps(response_json, indent=4)
    print(pretty_response)
    assert response.status_code == 200
    # jsonschema.validate(response_json, valid_schema)


def test_post():
    payload = {}
    url = "https://pay.test.bcdtravel.com/portal/users/settings"
    response = requests.post(url, )


@pytest.mark.suite_default
def test_swapi():
    response = requests.get("https://swapi.dev/api/people/1/")
    response_json = response.json()
    pretty_response = json.dumps(response_json, indent=4)
    print(pretty_response)
    assert response.status_code == 200
    jsonschema.validate(response_json, valid_schema)
    sch.close()


def test_open_file():
    file = open('../Resources/Schemas/people_info_schema.json')
    print('\n', type(file), '\n', file.read())
    file.close()


def test_os_name():
    print('\n', p.uname())

