#encoding=utf-8 
import unittest  
import json  
import requests  
from HTMLTestRunner import HTMLTestRunner
import time,sys,os
from config.Log import *
 #定义测试用例的目录为当前目录  
test_dir = './test_case'  
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')  
 
if __name__=="__main__":  
#     #按照一定的格式获取当前的时间  
#     now = time.strftime("%Y-%m-%d %H-%M-%S")  
#     print now
    #定义报告存放路径  
    filename ='/Volumes/forWork/python/interfacetest/src/test_report/TestRunner.html'  
    fp = open(filename,"wb")  
     #定义测试报告  
    runner = HTMLTestRunner(stream = fp,  
                            title='质控控城市接口测试报告',
                            description='测试用例执行情况:')  
    #运行测试  
    runner.run(discover)     
    fp.close() #关闭报告文件
    os.system("/Volumes/forWork/python/interfacetest/src/sendemail.py")
    logging.info(u"测试结束")