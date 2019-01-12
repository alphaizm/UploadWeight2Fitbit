# UploadWeight2Fitbit
fitbitへ体重をアップロードする

### 事前準備 ###
 　　→クライアントID、シークレットの取得(※)  
   　　→ **token.bat** と **PythonFitbit.py** 内の内容は更新  
 　　→体重計からの計測結果を準備(*.csv)  

------
### 手順 ###
　1. "token.bat" を実行  
　　→Webページが表示 →閉じる  
　　→コマンドライン画面が消えるのを待つ  
　2. "PythonFitbit.py"を実行  
　　→体重がfitbitへアップロードされる  

※クライントID、シークレットの取得についてや、環境作成については以下を参照  
https://pc.atsuhiro-me.net/entry/2014/05/07/022857

当方はVisual Studio 2017にて作成
