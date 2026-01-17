*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google And Search
    # Ignore SSL errors and open edge
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    
    Open Browser    https://www.google.com    edge    options=${options}
    Maximize Browser Window
    
    # Wait for the search bar to appear (Up to 10 seconds)
    Wait Until Element Is Visible    name=q    10s
    Input Text      name=q    Robot Framework Jira Integration
    Press Keys      name=q    ENTER
    
    Wait Until Page Contains    Robot Framework    10s
    Close Browser