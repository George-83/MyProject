# from data.imports import *
# from data.urls import *
#
#
# def test_my_communities():
#     driver.get(epam_community_url)
#     time.sleep(2)
#     driver.add_cookie(cookies)
#     # if we need to add several cookies, we should use next loop:
#     # for cookie in cookies:
#     #     driver.add_cookie(cookie)
#     driver.refresh()
#     time.sleep(2)
#     link_communities = driver.find_element(By.CLASS_NAME, 'evnt-my-communities')
#     assert link_communities is not None
#     assert link_communities.text == "MY COMMUNITIES"
#     link_communities.click()
#     assert driver.current_url == "https://wearecommunity.io/user-profile"
#     driver.close()
