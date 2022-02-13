# NTU-EXCHANGE-REVIEW 國立臺灣大學出國交換歷屆心得查詢器

+ [NTU-EXCHANGE-REVIEW 國立臺灣大學出國交換歷屆心得查詢器](#ntu-exchange-review-國立臺灣大學出國交換歷屆心得查詢器)
  + [Intro](#intro-專案起源)
  + [Tutorial](#tutorial-使用說明)
  + [Conclusion](#conclusion-專案結語)

## Intro 專案起源

此查詢器專為改善國立臺灣大學國際事務處所提供之「[歷屆交換學生名單及心得](https://oia.ntu.edu.tw/students/outgoing.students.experience)」，追加「以學校名稱進行搜尋」的功能及提供「過濾未繳交心得」的篩選選擇。

This tool aims at optimizing "Outgoing Students' Experience" provided by Office of International Affairs (OIA), National Taiwan University (NTU). Now "search with school name" and "filter experience not provided" are available here.

## Tutorial 使用說明
<img src="https://img.shields.io/badge/python-requests %7C BeautifulSoup4 %7C streamlit %7C pandas-blue">

> Tested on macOS High Sierra 10.13.6

1. Link to [NTU-EXCHANGE-REVIEW 國立臺灣大學出國交換歷屆心得查詢器](https://share.streamlit.io/damien-y/ntu-exchange-review/main.py)
開啟網頁
2. Check student identity (Summer School / Visit Student / Exchange Program)
勾選想查詢出國學生之身份（暑期 / 訪問 / 交換）
3. Input exchange school name (E.g. Chulalongkorn University)
輸入國外姐妹校之名稱（E.g. 朱拉隆功大學）
4. Successful! Scroll down to view those awesome experiences!
搜尋成功！下拉可看歷屆資料表格

**Other Information 其他說明**
- The year default is for recent 10-year data. It's allowable to choose years spanning from 1998 to 2022.
出國年度預設為近 10 年出國記錄，若有需求可以自行增減（87 年度 - 110 年度均有提供）
- Check "Only show experiences uploaded" and filter out datas that students did not submit their files.
勾選「僅顯示有繳交心得之結果」後即可過濾未繳交心得的資料列
- Refresh if any error messages pop out.
網頁操作時若有錯誤訊息，重新整理即可再次使用

## Conclusion 專案結語

這項簡單的查詢工具不只是想要嘗試提供學校以外更好使用的選項外，也是希望累積個人作品集。若你使用上遇到任何疑難雜症或是想要多瞭解的資訊可以透過 B06107054@ntu.edu.tw 聯繫專案作者。
This tool is not only trying to provide a better search experience, but also to beautify my portfolio. Please feel free to contact B06107054@ntu.edu.tw if you have any questions.

最後非常感謝處室願意提供出國機會，以及歷屆學長姐繳交的心得讓後面的學生可以有更多參考資訊。
Lastly, it's grateful that OIA gives NTU students chances to connect the world, and thoses useful experiences are so informative that we can plan our exhcange life in an effective and efficient way.

---
> Created by @Chun-Lin (Damien) Yu
