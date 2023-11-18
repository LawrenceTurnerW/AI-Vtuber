import requests
import json

base_url = "http://localhost:50021/"

text = "ボイスボックス"

#http://localhost:50021/speakers を参照
spealer_id = 2

aq_params = {
	'text':text,
	'speaker':spealer_id
}

#音声合成用のクエリ作成
res = requests.post(base_url+'audio_query',params=aq_params)
res_json = res.json()
print(res_json)

#作成したクエリを使って音声合成
s_params = {
	'speaker':spealer_id
}
res = requests.post(base_url+'synthesis',params=s_params,data=json.dumps(res_json))

print(res.content)