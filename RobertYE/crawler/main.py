from RobertYE.crawler.parser import Setting, GetJson, JsonToGetText

setting = Setting(open("QR.html"), "QR")#Setting(html,寫入檔名)
setting.set_tag("KGL-DOH 01 Apr 2018 Passenger,Freighter,Truck ")#設定要爬的文字
setting.set_tag_map({'Aircraft :B787': 2})#設定相同文字不同TAG set_tag_map({'TAG','第幾個'})
setting.set_table("Flight No")#設定要爬的Table的Title其中一個
setting.to_json()#輸出至檔案

json_str = GetJson("QR").to_string()#從檔案取的Json設定檔

print(json_str)

tag = JsonToGetText(open("QR.html"), json_str)#匯入設定檔
print(tag.get_tag_text())#取得Tag的文字
print(tag.get_table_text())#取得表格的二維陣列