import efinance as ef
from datetime import datetime
from efinance.fund.getter import get_base_info
import pandas as pd


class FundAction(object):
    ''
    fundCode = ''

    def __init__(self, fundCode):
        self.fundCode = fundCode

    def fetchHistory(self, startDate, fundCode=""):
        if(fundCode != ""):
            self.fundCode = fundCode

        fromDate = datetime.strptime(startDate, "%Y-%m-%d")
        toDate = datetime.today()
        pagesize = (toDate - fromDate).days
        history = ef.fund.get_quote_history(self.fundCode, pagesize)
        result = history.loc[pd.to_datetime(history['日期']) >= fromDate, ['日期', '单位净值', '涨跌幅']].sort_values(
            by='日期').reset_index(drop=True)
        return result

    def getFundName(self, fundCode=""):
        if(fundCode != ""):
            self.fundCode = fundCode
        return ef.fund.get_base_info(self.fundCode)['基金简称']

# pagesize = (currentDate - fromDate).days

# history = ef.fund.get_quote_history(fundcode, pagesize)

# result = history.loc[:, ['日期', '单位净值', '涨跌幅']
#                      ].sort_values(by='日期').reset_index(drop=True)

# result.to_excel('基金.xlsx', fundcode)
