    for max_num_comment in driver.find_element_by_xpath("//tbody/tr/td"):
        max_num = max_num_comment.text
        max_num = max_num.replace(" ", "")
        print("----------------------")
        print(max_num_comment)#text
        print("----------------------")