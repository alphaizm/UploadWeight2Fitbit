import csv
import pandas as pd
import re
from pathlib import Path
import glob

def main():
	p_file = Path(__file__)
	p_work = Path(p_file.parent)

	str_token_access = ""
	str_token_refresh = ""
	
	# 以下のトークンを取得
	#	・アクセストークン
	#	・リフレッシュトークン
	str_token_access, str_token_refresh = funcGetToken(p_work)

	print("アクセストークン：" + str_token_access)
	print("リフレッシュトークン：" + str_token_refresh)

	# アップロード用の体重リストをCSVから取得
	lst_wight_log = funcGetWeightList(p_work)


#######################################
###	トークン文字列の取得
def funcGetToken(p_work):
	for p_txt in list(p_work.glob("*.txt")):
		str_ret_access = ""
		str_ret_refresh = ""

		#print(p_txt)
		txt_file = open(p_txt,"r")
		lines = txt_file.readlines()
		txt_file.close()

		for line in lines:
			if "" == line:
				continue

			if "access_token" in line:
				str_ret_access = getToken(line)
			elif "refresh_token" in line:
				str_ret_refresh = getToken(line)

	return str_ret_access, str_ret_refresh

#######################################
###	体重リスト配列の取得
def funcGetWeightList(p_work):

	lst_str_ret_lines = list()

	for p_csv in list(p_work.glob("*.csv")):
		print(p_csv)
		csv_file = open(p_csv, "r")


		###################################
		#   CSVフォーマット
		###################################
		#[0] 日付 →YYYY／mm／DD
		#[1] 計測時刻 →HH：MM：SS ※未計測時：00:00:00
		#[2] 体重(kg) →xx.xx
		#[3] BMI →xx.x
		#[4] 体脂肪率(%) →xx.x
		#[5] 骨格筋率(%) →xx.x
		#[6] 基礎代謝(kcal) →xxxx
		#[7] 内臓脂肪レベル →x.x
		#[8] 体年齢(才) →xx
		#[9] 取込分類' →ファイル
		#[10] 取込日時 →YYYY／mm／DD HH:MM
		#[11] 機器名 →HBF-252F
		#[12] シリアル →0C0B1B0F3701
		#[13] 個人番号 →1
		for row in csv.reader(csv_file):

			lst_str_cells = list()

			cells = [line.split(",") for line in row]

			if 4 <= len(cells):
				str_date = funcGetList2str(cells[0])
				str_time = funcGetList2str(cells[1])
				str_weight = funcGetList2str(cells[2])
				str_fat = funcGetList2str(cells[4])
				if "00:00:00" != str_time:
					regex_date = re.match(r"\d{4}/\d{2}/\d{2}", str_date)
					if regex_date:
						if "" != str_weight:
							if "" != str_fat:
								#str_disp = str_date.replace(r"/", r"-") + " → " + str_weight + " ／ " + str_fat
								#print(str_disp)

								#各セル内容を格納
								lst_str_cells.append(str_date.replace(r"/", r"-"))
								lst_str_cells.append(str_weight)
								lst_str_cells.append(str_fat)

								#1行分を格納
								lst_str_ret_lines.append(lst_str_cells)
					#else:
					#	str_disp = str_date + " → " + str_weight + " ／ " + str_fat
					#	print(r"ヘッダー行：" + str_disp)
		csv_file.close()

	return lst_str_ret_lines

#######################################
#	トークン文字列取得
def getToken(str_):
	str_ret = ""
	str_rep = str_.replace(r" ",'')
	ary_str_split = re.split(r"[=\n]",str_rep)
	#for disp in ary_str_split:
		#print(disp)

	if 1 <= len(ary_str_split):
		str_rep = ary_str_split[1]

	return str_rep


#######################################
#	リストから文字列取得
def funcGetList2str(cell_):
	return re.sub(r"[\[\]\']", "", str(cell_))


#main()