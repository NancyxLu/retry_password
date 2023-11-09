#密碼重試

#程式已設定密碼 為 a123456
#使用者有三次機會可輸入
#若輸入錯誤 顯示 "密碼錯誤!還有___次機會"
#若輸入正確 顯示 "登入成功!"

checked_pwd = 'a123456'
count = '3'
count = int (count)

user_pwd = input ('請輸入密碼:')
while user_pwd != checked_pwd and count > 0: 
	count = count - 1
	print ('密碼錯誤!')
	if count > 0:
		print ('還有', count, '次機會')
		user_pwd = input ('請輸入密碼:')
	else:
		print ('請聯絡資訊人員重設密碼')
if user_pwd == checked_pwd :
	print ('登入成功')