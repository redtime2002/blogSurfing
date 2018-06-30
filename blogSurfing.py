from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from operator import eq
from random import randint

import time

receiver = "test_lee3@naver.com"
sender = "test_lee2@naver.com"

receiverId = "test_lee3"
senderId = "test_lee2"

receiverPw = "naver!23"
senderPw = "naver!23"

tmpTime = ""

IdList = ["test_lee2" , "test_lee3", "redtime2002"]
pwList = ["naver!23", "naver!23", "dlwlssud9089!"]

searchList = ["안개속의숙녀호", "나이아가라폭포", "혼블라워",
              "프라임 타파웨어", "스마트 그릴", "월스트리트", "원적외선 쿡탑",
              "마리나시티", "한국전쟁참전용사기념관", "디스틸러리디스트릭트",
              "소어산공원", "루쉰공원", "피차이위엔거리", "링컨기념관",
              "스미스소니언박물관", "스텔렌보쉬", "빅캣파크",
              "커스텐보쉬", "타파웨어"]

driver = webdriver.Chrome("C:\selenium\chromedriver.exe")


def logIn(Id, Pw):
    driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[1]/div/a/span").click()
    waitForIsElementPresent("//*[@id='id']")

    driver.find_element_by_xpath("//*[@id='id']").send_keys(Id)
    driver.find_element_by_xpath("//*[@id='pw']").send_keys(Pw)

    driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click();


def logOut():
    driver.find_element_by_xpath("//*[@id='gnb_name1']").click()
    driver.find_element_by_xpath("//*[@id='gnb_logout_button']/span[3]").click()


def waitForIsElementPresent(xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print(xpath, "가 존재하지 않습니다.")
        driver.close()


def basicWriting():
    driver.find_element_by_xpath("//*[@id='toInput']").send_keys(receiver)

    time.sleep(1)

    driver.find_element_by_xpath("//*[@id='atcp']/ul/li/div/a").click()
    driver.find_element_by_xpath("//*[@id='subject']").click()

    curTime = time.strftime("%Y%m%d %H%M%S", time.localtime())
    tmpTime = curTime

    driver.find_element_by_xpath("//*[@id='subject']").send_keys(curTime)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='se2_iframe']"))
    driver.find_element_by_xpath("/html/body").send_keys(curTime)

    driver.switch_to_default_content()

def focus_this_Window():
    handles = driver.window_handles
    driver.switch_to.window(handles[len(handles)-1])



# 대화형 메일 만들기
def makeConversation(num):
    driver.get("http://mail.naver.com")

    logIn(senderId, senderPw)

    driver.find_element_by_xpath("//*[@id='nav_snb']/div[1]/a[1]/strong").click()
    waitForIsElementPresent("//*[@id='toInput']")

    basicWriting()

    driver.find_element_by_xpath("//*[@id='sendBtn']").click()

    waitForIsElementPresent("//*[@id='sendresultDivContent']/div[2]/h4")
    comment = driver.find_element_by_xpath("//*[@id='sendresultDivContent']/div[2]/h4").text

    assert eq(comment, "메일을 성공적으로 보냈습니다.")

    i = 0

    while num > i:

        logOut()
        waitForIsElementPresent("//*[@id='container']/div/div[2]/div[1]/div/a/span")

        if i % 2 == 0:
            logIn(receiverId, receiverPw)
        else:
            logIn(senderId, senderPw)

        driver.find_element_by_xpath("//*[@id='nav_snb']/div[3]/div/div[1]/ul/li[1]/span/a[1]").click()

        waitForIsElementPresent("//*[@id='list_for_view']/ol/li[1]/div/div[2]")
        driver.find_element_by_xpath("//*[@id='list_for_view']/ol/li[1]/div/div[2]").click()

        waitForIsElementPresent("//*[@id='readBtnMenu']/div[1]/span[1]/button[1]")
        driver.find_element_by_xpath("//*[@id='readBtnMenu']/div[1]/span[1]/button[1]").click()

        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='sendBtn']").click()
        waitForIsElementPresent("//*[@id='sendresultDivContent']/div[2]/h4")
        comment = driver.find_element_by_xpath("//*[@id='sendresultDivContent']/div[2]/h4").text

        if eq(comment, "메일을 보내지 못했습니다."):
            driver.find_element_by_xpath("//*[@id='sendresultDivContent']/div[2]/p[2]/a").click()
            waitForIsElementPresent("//*[@id='list_for_view']/ol/li[1]/div/div[2]/a/span/strong")
            driver.find_element_by_xpath("//*[@id='list_for_view']/ol/li[1]/div/div[2]/a/span/strong").click()

            time.sleep(1)

            driver.find_element_by_xpath("//*[@id='sendBtn']").click()

        elif eq(comment, "메일을 성공적으로 보냈습니다."):
            assert eq(comment, "메일을 성공적으로 보냈습니다.")

        i = i + 1
        time.sleep(1)



#   블로그 서핑
def surfingBlog():

    for i in range(0, 100):

        driver.get("http://www.naver.com")

        time.sleep(1 + randint(0, 2))

        if i != 0 :
            driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='minime']"))

            waitForIsElementPresent("//a[@id='btn_logout']")
            driver.find_element_by_xpath("//a[@id='btn_logout']").click()

            driver.switch_to.default_content()

        time.sleep(1 + randint(0, 1))

        waitForIsElementPresent("//input[@id='id']")

        loginRand = randint(0, len(IdList)-1)
        driver.find_element_by_xpath("//input[@id='id']").send_keys(IdList[loginRand])
        driver.find_element_by_xpath("//input[@id='pw']").send_keys(pwList[loginRand])

        time.sleep(1 + randint(0, 1))

        driver.find_element_by_xpath("//input[@title='로그인']").send_keys(Keys.ENTER)

        time.sleep(1)

        rand = randint(0,len(searchList)-1)

        print();
        print("************* " + str(i+1) +"번째 검색어 : " + searchList[rand] + "*************")
        driver.find_element_by_xpath("//input[@id='query']").send_keys(searchList[rand])
  #      time.sleep(1 + randint(0, 2))



        driver.find_element_by_xpath("//button[@id='search_btn']").send_keys(Keys.ENTER)
  #      time.sleep(1 + randint(0, 2))

        driver.find_element_by_xpath("//span[text()='블로그']").click()

        for page in range (1,100):
            print("***** " + str(page) + "번째 페이지 *****")

            cnt = 0
 #           time.sleep(5 + randint(0, 3))

            bloglist = driver.find_elements_by_xpath("//li[@class='sh_blog_top']")

            for j in range(0, len(bloglist)):

                print(bloglist[j].find_element_by_xpath("dl/dd/span/a[1]").text)
                if eq(bloglist[j].find_element_by_xpath("dl/dd/span/a[1]").text, "dooboorang"):
                    bloglist[j].find_element_by_xpath("dl/dt/a").click()
                    cnt = 1

                    focus_this_Window()

  #                  time.sleep(10 + randint(0, 10))

 #                   time.sleep(10 + randint(0, 10))

                    driver.close()

                    focus_this_Window()

                    break

            # dooboorang 있었을 경우
            if cnt == 1:
                break
            else:
                driver.find_element_by_xpath("//a[text()='다음페이지']").click()
                continue

  #  time.sleep(10)




surfingBlog()

driver.close()