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
    set window size        width=1600   height=1000

    sleep                  1s
    page should contain    We Are Dedicated to Parking
    click link             xpath=//*[@id="wrap"]/div[1]/div/div[3]/ul/li[2]/a
    page should contain    Classic & Muscle Cars for Sale
    click element          xpath=//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[2]/ul/li/a
    click link             Ford
    close browser


*** Keywords ***
