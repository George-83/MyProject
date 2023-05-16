*** Settings ***
Library             SeleniumLibrary

*** Keywords ***
Load
    go to                  ${START_URL}


Verify Page Loaded
    page should contain    We Are Dedicated to Parking