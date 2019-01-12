import fitbit
import openFile
from pathlib import Path

def main():
	p_file = Path(__file__)
	p_work = Path(p_file.parent)

	CLIENT_ID = ''
	CLIENT_SECRET = ''

	#各トークンをファイルから取得
	ACCESS_TOKEN, REFRESH_TOKEN = openFile.funcGetToken(p_work)

	client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,
						access_token=ACCESS_TOKEN,
						refresh_token=REFRESH_TOKEN,
						system="ja-JP")

	# アップロード用の体重リストをCSVから取得
	lst_wight_log = openFile.funcGetWeightList(p_work)

	for idx, line in enumerate(lst_wight_log):
		cell = openFile.funcGetList2str(line).split(",")

		if 3 <= len(cell):
			print("\t→" + cell[0])

			client.body(date=cell[0], data={"weight":cell[1], "fat":cell[2]})

main()