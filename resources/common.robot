*** Settings ***
Library             SeleniumLibrary

*** Keywords ***
Begin Web Test
    #Selenium speed - this is speed of execution steps, sets the delay that is waited after each Selenium command)
    set selenium speed     .2s
    set selenium timeout   10s
    log                    Starting the test case
    open browser           about:blank  ${BROWSER}
    #Setup creen size
    #set window size        width=1600   height=1000
    maximize browser window

End Web Test
    close browser
