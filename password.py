# 密碼重試程式
# password = a123456
# 最多輸入3次
# 正確 就顯示”登入成功！“
# 錯誤 就顯示“密碼錯誤！re還有＿次機會“

password = 'a123456'
chance = 3 # 剩餘的機會

while chance > 0:
	enter = input('請輸入密碼:') 
	chance = chance - 1 

	if enter == password:
		print('登入成功！')
		break # 結束while迴圈
	else:
		print('密碼錯誤！')
		if chance > 0:
			print('還有', chance, '次機會')
		else:
			print('Locked!')