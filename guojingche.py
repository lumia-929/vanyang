#coding=utf-8
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from  HTMLTestRunner import HTMLTestRunner
import time

class gjc (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://192.168.200.143:8070/brain-h5/panel/")
        sleep(4)
        #js="document.body.style.zoom='0.4'"
        #cls.driver.execute_script(js)
        #sleep(2)

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass



    def test_02(self):
        '''选择过境车'''
        driver=self.driver
        #先移动过去页面再去点击
        js="window.scrollBy(1400,0)"
        driver.execute_script(js)
        sleep(1)
        #点击右边箭头，把过境车元饼图开出来
        trangel=driver.find_element("xpath","//*[@id='app']/div/div[11]/span[3]")
        i=0
        while i<15:
            trangel.click()
            i=i+1
            sleep(0.5)

        #点击过境车的元饼图
        circle=driver.find_elements("tag name","span")

        for guojc in circle:
            if guojc.get_attribute("data-index")=="28":
                guojc.click()


    def test_01(self):
        '''点击下拉篮'''
        driver=self.driver
        driver.find_element("xpath","//*[@id='app']/div/div[11]/span[1]").click()
        sleep(0.5)

    def test_03(self):
        '''判断是否成功打开过境车功能模块'''
        driver=self.driver
        driver.execute_script("window.scrollTo(0,0)")
        sleep(1)
        title=driver.find_element("xpath","//*[@id='app']/div/div[9]/div[1]/div/div/div/div[1]/div[1]/div[1]").text
        print(title)
        #通过标题名字是否带有过境2字进行判断是否成功打开过境车模块
        try:
            self.assertIn("过境",title)
            print("成功打开过境车模块")
        except Exception as msg:
            print("打开过境车模块失败")
            print("失败原因：%s"%msg)

    def test_04(self):
        '''进入到过境两客车辆'''
        driver=self.driver
        driver.execute_script("window.scrollTo(7000,700)")
        sleep(1)
        WebDriverWait(driver,10).until(lambda x:x.find_element("xpath","//*[@id='app']/div/div[10]/div[1]/div/div/div/div[4]/div[2]/div[1]/div[1]")).click()
        driver.execute_script("window.scrollTo(7000,0)")
        driver.implicitly_wait(20)
        driver.find_element("css selector","#app > div > div.chart-wrapper.right.show-TransitVehiclePush > div.TransitVehiclePush_show.chart-box > div > div > div.title-wrap > div.title-right > div.time-select > div:nth-child(3)").click()
        driver.execute_script("window.scrollTo(7000,800)")
        sleep(0.5)
        try:
            check=WebDriverWait(driver,10).until(lambda x:x.find_element("xpath","//div[@class='inset-shadow']/div/div[2]/div/div[4]/div[2]/div/div/table/tr[1]/td[5]"))
            check.click()
            print("年接口速度在接受范围内")
        except Exception as msg:
            print("接口查询超时")
            print("报错原因：%s"%msg)

if __name__=="__main__":
    suite=test=unittest.TestSuite()
    test.addTest(gjc("test_01"))#添加gjc类里面的def模块
    test.addTest(gjc("test_02"))
    test.addTest(gjc("test_03"))
    test.addTest(gjc("test_04"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    file='D:\\python\\WTF`S'+now+'testReport.html'#保存文件的地址和时间+文件名字
    van=open(file,'wb')
    runner=HTMLTestRunner(stream=van,title="乌蝇哥的日常生活报告",description="乌蝇哥的日常生活操作")
    runner.run(suite)
    van.close()


