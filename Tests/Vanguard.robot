*** Settings ***
Documentation       This is some basic information about whole suite
Library             SeleniumLibrary

#To run the test type in console: robot -d results tests/Vanguard.robot

*** Variables ***


*** Test Cases ***
Name of test - some test
    [Documentation]         This is some basic info about the test
    [Tags]                  1006    Smoke   HomePage

    #Selenium Setup (selenium speed - this is speed of execution steps, sets the delay that is waited after each Selenium command)
    set selenium speed      .2s
    set selenium timeout    10s

    log                     Starting the test case
    open browser            https://www.vanguardmotorsales.com/     chrome

    #Setup creen size
    set window position    x=341    y=169
    set window size        width=1500   height=1000

    sleep                  3s
    close browser


*** Keywords ***
