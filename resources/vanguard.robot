*** Settings ***
Library             SeleniumLibrary
Resource    ../Resources/PO/HomePage.robot

*** Keywords ***
Search For Ford Model
    HomePage.Load
    sleep                  1s
    HomePage.Verify Page Loaded
    click link             xpath=//*[@id="wrap"]/div[1]/div/div[3]/ul/li[2]/a
    page should contain    Classic & Muscle Cars for Sale
    click element          xpath=//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[2]/ul/li/a
    click link             Ford

Search 1965 Year
    click element          xpath=//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li/a
    click element          xpath=//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li/ul/li[5]/a
    page should contain element    xpath=//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div[1]/a
