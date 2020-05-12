#coding=utf-8
import requests
# from urllib.request import quote, unquote
import json
import os
import time

# keywords = ["书包", "雨伞"]
# for item in keywords:
#     word = item

def search(lines):
    leng = 9
    wdata = []
    for i in lines:
        word = i.strip('\n')
        print("读取到的一行：")
        print(word)
    # word = "书包"
        
        url = "http://yangkeduo.com/proxy/api/search_suggest?pdduid=0&query=" + \
            word + "&plat=H5&source=index"
        r = requests.get(url)
        # print(r.text)
        # print("=======")
        data = json.loads(r.text)
        # print(data['suggest_list'][0]['item_data']['suggestion'])
        # print("=======")
        # for i in data['suggest_list']:
        #     print(i['item_data']['suggestion'])
        # print("=======")
        length = len(data['suggest_list'])
        print(length)
        for i in range(length):
            
            if i < leng:
                item_data = data['suggest_list'][i]['item_data']
                # print("内容：")
                # print(item_data)
                # try:
                #     sug = item_data['suggestion']
                #     print("一条内容：")
                #     print(sug)
                # finally:
                #     pass
                
                if 'suggestion' in item_data:
                    sug = item_data['suggestion']
                    print("一条内容：")
                    print(sug)
                    wdata.append(sug)
        print("=======")
        # time.sleep(1)
    return wdata


if __name__ == "__main__":
    with open('./read.txt', 'r') as rf:
        lines = rf.readlines()
        line_num = len(lines)
    # print("读出的内容：")
    # print(lines)
    with open('./data.txt', 'w') as wf:
        wdata = search(lines)
        for i in range(len(wdata)):
            wf.write(str(wdata[i]) + '\n')
        # wf.write('two')
    
