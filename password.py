# 密碼重試程式
# password = a123456
# 最多輸入3次
# 正確 就顯示”登入成功！“
# 錯誤 就顯示“密碼錯誤！”還有＿次機會“

password = 'a123456'
chance = 3

while chance > 0:
	enter = input('請輸入密碼:') 

	if enter == password:
		print('登入成功！')
		break # 結束while迴圈
	else:
		chance = chance - 1 
		print('密碼錯誤！還有', chance, '次機會。')