*** Settings ***
Library    RequestsLibrary


*** Variables ***
${URL} =    https://swapi.dev/api/people/1/


*** Test Cases ***
Success GET request to swapi/pepole
    ${response} =    GET    ${URL}
    ${response_body} =  Set Variable    ${response.content}
    ${response_json} =  Evaluate    json.dumps(${response_body}, indent=4)
    log to console    \n${response_json}
    Log    \n${response_json}


*** Keywords ***
