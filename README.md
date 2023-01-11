# AutoSave

## 動機
解決忘記儲存的問題或是特定 檔案類型/檔案 實施版本管控

切記本程式一切的所有更新都只是為了讓 Hebearo 過得更自在，因此看不懂或不同意的部份請自行加油

## 使用目的
本程式使用之目的為自動監聽部份檔案類型/特定檔案 並存檔。最近幾次的更新會往 OneDrive 上備份，實現多平台/跨平台的檔案傳遞
## 使用原理

監聽"最近的項目 ( recent )"資料夾，這本是windows 自主監聽更改項目的捷徑庫，本程式AutoSave會持續監聽捷徑所指向之原始檔，若有更動則自動備份乙次。

目前已知最大問題即是檔案名稱必須是"完全不重複" 才能正常運作。
ex.
最近修改了 main.pptx , main.py 兩種不同檔案，而兩個檔案的捷徑名稱都將會是 main.lnk，因此最近的項目裡必然會捨棄其中一個並無法同時監聽。

## 備份成校
建議自主跑過一輪則知道

## 使用方法

1. 安裝requirements.txt 裡面的東西
2. 更改 coefficient 裡面的部份參數，請注意該路徑是否存在
3. run main_v3.py



------
## 以下為一些進度紀錄
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
2. 下一步要開始注意神抹檔案要存神抹不要。 （ 以完成 ）
3. 備份的檔案會叫做 'backed_...'作為跟原本檔案的區分。
下午17：00
發現最嚴重的問題：
 recent 不會區分同黨明得東西： 若檔案都叫做 some result，則其中一個必定被刪除，且被刪除的永遠不會被復原！！
下次在繼續努力！

2022/11/13
1. 更新 增加注意特殊檔案的公用
2. 發現無法定義追蹤資料夾
2022/11/15
1.新增儲存方式： hist, repl

2022/11/21
1.新增儲存地點設定 -> 從 ./backup_forder 轉移到任意想轉移的地方



2023/01/11
1. 新增掃描變化時間的間距為自由度放到 coefficient.py 裡面 ( x )
