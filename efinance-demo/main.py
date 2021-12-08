from fund import FundAction
import pandas as pd
from os import path, remove

import logging
import time

mylog = logging.getLogger('mylogger')
mylog.setLevel(logging.DEBUG)
# 处理器
handler = logging.FileHandler(
    'E:\development\python\efinance-demo\log_test.txt')
handler.encoding = 'UTF-8'
handler.setLevel(logging.DEBUG)
# 格式器
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
mylog.addHandler(handler)


fundExportPath = "E:\development\python\efinance-demo\基金.xlsx"
fundList = {'001617': '2021-07-28',
            '010202': '2021-08-17',
            '001593': '2021-07-28',
            '110003': '2021-07-28',
            '110026': '2021-07-28',
            '110022': '2021-07-28',
            '013304': '2021-09-03'

            }


def generateFundExcel():
    with pd.ExcelWriter(fundExportPath) as writer:
        for code, trackStartDate in fundList.items():
            mylog.debug("~~~~~~~~~ 开始获取基金:" + code +
                        ",获取 " + trackStartDate + "之后的基金数据:")
            fund = FundAction(code)
            fundName = fund.getFundName()
            fundHistory = fund.fetchHistory(trackStartDate)
            fundHistory["涨跌幅"] = pd.to_numeric(
                fundHistory["涨跌幅"], errors="coerce").fillna(0)
            fundHistory['累计涨跌'] = fundHistory["涨跌幅"].cumsum()
            # fundHistory.append([{"total", fundHistory.sum('涨跌幅')}])
            fundHistory.to_excel(writer, sheet_name=fundName)
            mylog.debug("==============加载基金：" +
                        code + " 完成===================")


def run():
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    mylog.debug(f'log start {start_time}')
    generateFundExcel()
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    mylog.debug(f'log ended {end_time}')
    mylog.debug('\n')


run()
