*** Settings ***
Library    RequestsLibrary


*** Variables ***
${URL} =    https://swapi.dev/api/people/1/


*** Test Cases ***
Success GET request to swapi/pepole
    ${response} =    GET
*** Keywords ***
