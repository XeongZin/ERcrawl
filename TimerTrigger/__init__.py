import csv
import datetime
import imp
import json
import logging
import sys
import time
import os
from encodings import utf_8_sig  # 액셀파일에서 한글깨질때

import azure.functions as func
import requests
from bs4 import BeautifulSoup
from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError

sys.path.append("./")
from . import er_crawling

def main(mytimer: func.TimerRequest, tablePath:func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()


    if mytimer.past_due:
        logging.info("The timer is past due!")

    logging.info("Python timer trigger function ran at %s", utc_timestamp)

    tags = er_crawling.scrape_ER
    er_data = {
        "미국 단위 당":tags[0],
        "한국 원":tags[1],
        "전일 대비 상승 하락":tags[2],

        "일본 단위 당":tags[3],
        "한국 원":tags[4],
        "전일 대비 상승 하락":tags[5],

        "유럽 연합 단위 당":tags[6],
        "한국 원":tags[7],
        "전일 대비 상승 하락":tags[8],

        "중국 단위 당":tags[9],
        "한국 원":tags[10],
        "전일 대비 상승 하락":tags[11],

        "영국 단위 당":tags[12],
        "한국 원":tags[13],
        "전일 대비 상승 하락":tags[14],

        "호주 단위 당":tags[15],
        "한국 원":tags[16],
        "전일 대비 상승 하락":tags[17],

        "캐나다 단위 당":tags[18],
        "한국 원":tags[19],
        "전일 대비 상승 하락":tags[20],

        "뉴질랜드 단위 당":tags[21],
        "한국 원":tags[22],
        "전일 대비 상승 하락":tags[23],

        "태국 단위 당":tags[24],
        "한국 원":tags[25],
        "전일 대비 상승 하락":tags[26],

        "베트남 단위 당":tags[27],
        "한국 원":tags[28],
        "전일 대비 상승 하락":tags[29],

        "홍콩 단위 당":tags[30],
        "한국 원":tags[31],
        "전일 대비 상승 하락":tags[32],

        "대만 단위 당":tags[33],
        "한국 원":tags[34],
        "전일 대비 상승 하락":tags[35],

        "PartitionKey":"Exchange_Rate",
        "RowKey": time.time()
    }
    print("new_data=",er_data)

    tablePath.set(json.dumps(er_data))