# AutoSave


2022/11/11
1. 嘗試開始現正恢復所有時間序列監聽 main_v2.py （未完成）
2. 完成掃描資料夾 （Package.py , main_v2)


2022/11/12
1. 開始嘗試只抓取特定檔案類型 .pptx
2. move main.py, main_v3.py -> abandonded

3. 以下先暫定 main_v3 將會是第一個完整版：

只監聽部份開啟 python 定義的部份檔名：
並非持續更新所有檔案，而是建立現有的Lnk （FileLnk_dict）資料庫，並反覆去監聽，開啟以後持續監聽，dict 大小只會減少不會增加。

現已完成 main_3 其監聽功能 ( 若檔案在時間內改動會抓的到）
下一步為增加備份的功能
部份在 FileLnk 裡面加入的 try except 是要阻止：
    a. 有 Windows 內建的檔案或資料夾掉入
    b. 檔案已不存在或其他東西

下午16：00
1. 建立 backup_folder, 並已經用 gitignore 忽略以後存入的檔案
2. 下一步要開始注意神抹檔案要存神抹不要。