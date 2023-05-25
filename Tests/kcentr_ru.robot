*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String
Library    JSONLibrary
#To run the test type in console: robot -d results tests/kcentr_ru.robot

*** Variables ***
${URL} =    https://kcentr.ru/content-service/api/desktop/v1/products?visitorUuid=8485f7ea-f2e7-4478-aff3-e8fe3b0f3cf0&cityUuid=deb1d05a-71ce-40d1-b726-6ba85d70d58f&categoryId=televizory&sortType=price_asc&limit=19

*** Test Cases ***
GET request price_asc
    Create Session  my session  ${URL}}
    ${response} =    GET  ${URL}
    ${response_body}    set variable    ${response.content}
    ${response_json}    set variable    evaluate    json.loads('''${response_body}''')
    ${sorted_response}    sort list    ${response_json}    key=lambda x: x['price']
    log    ${sorted_response.json()}
    log to console   ${sorted_response.json()}



*** Keywords ***
