*** Settings ***

Documentation       This is some basic information about whole suite
Resource    ../Resources/Vanguard.robot
Resource    ../Resources/Common.robot
Test Setup    Begin Web Test
Test Teardown    End Web Test
#To run the test type in console: robot -d results tests/Vanguard.robot

*** Variables ***
${BROWSER} =    chrome
${START_URL} =    https://www.vanguardmotorsales.com/

*** Test Cases ***
Name of test - Search for Ford
    [Documentation]         Some other information
    [Tags]                  Smoke   HomePage
    Vanguard.Search For Ford Model


Name of test - Search for Ford car 1965
    [Documentation]         Some other information
    [Tags]                  Smoke   HomePage
    Vanguard.Search For Ford Model
    Vanguard.Search 1965 Year
