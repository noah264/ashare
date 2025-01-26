from flask import jsonify
from flask_restful import Resource
import akshare as ak
import pandas as pd
import json


class AshareList(Resource):
    def get(self):
        try:
            # 获取所有股票代码和名称
            stock_info_a_code_name_df = ak.stock_info_a_code_name()

            stock_info_a_code_name_df.set_index('code', inplace=True)

            # 初始化一个空的字典来存储所有股票数据
            all_stock_data = {}


            # 遍历股票代码获取数据
            for stock_code in stock_info_a_code_name_df.index:
                try:
                    # 获取股票历史数据
                    stock_data = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date="20240101",
                                                    end_date="20241231")
                    # # 将数据转换为 JSON 格式
                    stock_data_json = stock_data.to_dict(orient='records')
                    # # 将 JSON 数据存储到字典中
                    all_stock_data[stock_code] = stock_data_json
                except Exception as e:
                    print(f"获取股票 {stock_code} 的数据时出错: {e}")

            # 返回 JSON 数据
            print(all_stock_data)
            # return jsonify(all_stock_data)
        except Exception as e:
            return jsonify({"error": str(e)})

        return "",200
