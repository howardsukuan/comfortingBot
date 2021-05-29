# LINE 檔案使用說明
## 1. 檔案內容
在這個資料夾中，攸關建置 LINE chatbot 的主要有一個資料夾以及三個 .py 檔：```intent```、```app_line.py```、```comfortingREF.py```、```comforting_bot_for_loki.py```。

## 2. 環境設定
若想在 LINE 上建置自己的 chatbot，請參考下列步驟：

1. 請至 LINE Developers (https://developers.line.biz/zh-hant/)，登入您的 LINE 帳號。

2. 登入後，點選橫幅選單列中的 Products，並選擇 Messaging API，最後按下 Start now (如以下圖1.圖2所示)。

***圖 1. Products 介面***

![](https://upload.cc/i1/2021/05/25/EPKCRS.png)

***圖 2. Messaging API 介面***

![](https://upload.cc/i1/2021/05/25/fVtvlw.png)

3. 在 Create a channel 中需填寫必要的資訊(每個必填項目請於下方查看更進一步的詳細說明)。在填寫完畢後，需確實了解 LINE Official Account Terms of Use 和 LINE official Account API Terms of Use，最後點 Create 送出資料。

* Channel type: 系統已自動選取 Messaging API 了。
* Provider: 請選擇 Create a new provider，並於下方自行取名 (以圖3為例，取名為 comfortingBot)。

***圖 3. 設定 provider 之範例***

![](https://upload.cc/i1/2021/05/25/axnGhP.png)
 
* Channel name: 請於此打上您 LINE chatbot 的名字。
* Channel description: 請描述此 chatbot 之用途。
* Category: 請選擇您的 chatbot 所服務的內容範圍 (例如：生活相關服務)。
* Subcategory: 請選擇細項的服務內容 (例如：相親、交友服務)。

4. 在 Basic settings 中，可以找到您的 Channel secret，這是一組重要的密碼，因為若是擁有這組密碼就等同擁有進入您的 chatbot 的權限。您可以建立一個密碼檔案，儲存所有的密碼資料。

5. 在 Messaging API 中，可以到到您的 Channel access token，這一大串文字也是 chatbot 的密碼，您需要結合上面提及的 Channel secret (第4點)，兩組密碼同時輸入才能找到您的 chatbot。

6. 另外，在 LINE Developers 中，您需要架設一個 Server，建議您可以選擇 Heroku 作為 Server。詳細步驟請參考以下書籍 -- *LINE Bot by Python 全攻略* (作者饒孟桓)。

7. 最後，若 Webhook 顯示成功，此 chatbot 就可以在 LINE 中運作了！

## 3. 檔案內容指引 (檔案按字母順序排列)
```app_line.py```：
此程式碼用於連接 `comforting_bot_for_loki.py` 與 LINE 上的 chatbot ，詳細說明亦可以從前面提到的參考書 (*LINE Bot by Python 全攻略*) 查詢。

```clock.py```：
免付費 Heroku 上面的專案只要在閒置狀態超過30分鐘就會自動休眠，直到下次被觸發時才會甦醒。此程式碼會每二十分鐘喚醒 LINE，避免程式因為閒置過久進入自動休眠。

```comforting_bot_for_loki.py```：
此程式碼有三個重要的 function：<font color=#FF00FF>runLoki</font>、<font color=#FF00FF>HandleFeelings</font> 以及 <font color=#FF00FF>HandleReasons</font>。其中，第 180 行的 <font color=#FF00FF>runLoki</font> 在一個句子進來時，讓 chatbot 自動抓取關鍵字並與 ```comfortingREF.py``` 中的資料比對，給予相對應的回覆。
因此，第 218 行的 <font color=#FF00FF>HandleFeelings</font> 就是用於偵測及抓取情緒相關的關鍵字，而第 255 行的 <font color=#FF00FF>HandleReasons</font> 則是用於偵測及抓取抱怨緣由的關鍵字。

```comfortingREF.py```：
此程式碼存放所有我們定義的 <font color=#FF00FF>LIST</font> 與 <font color=#FF00FF>DICT</font>，包含用於偵測及判斷抱怨語句的關鍵字，以及對應不同抱怨緣由的回覆。

```intent```資料夾：
這個資料夾中存取了我們所有的抱怨語句，其中包含與情緒相關的句子 (例如：我心情不好)，以及心情不好的原因 (例如：我考試考差了)。

```Procfile```：
此指令告訴 Heroku 我們的應用程式是哪種類型的應用程式，以及需要執行哪個檔案。我們的 LINE chatbot 是 web 類型的應用程式，且需要透過`app_line.py`執行。
此外，我們也執行`clock.py`，避免 LINE 因為閒置狀態過久進入自動休眠。

```requirement.txt```：
此檔案告訴 Heroku 需要安裝哪些套件，以及該套件版本。

```runtime.txt```：
此檔案告訴 Heroku 我們用來執行應用程式的 Python 版本。
