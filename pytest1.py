#encoding:UTF-8
#编写登录密码
#认证成功后显示欢迎信息
#输入错误三次后锁定
def denglu():                                     #写错过 没加()
	pass_world=raw_input("please input your passworld:")
	if pass_world=="12.34":
		print("yes,the passworld is OK ,you can do it now")
	if pass_world!="12.34":                     #这里出现语法无效   落了一个冒号
		print("please try again")
		count=3
		count=count-1
		if count==0:
			print("you have no time")
			#break
		#break

#这里用1代表一级目录1.1代表二级目录1.1.1代表三级目录
#这里写1，2，3三个一级目录，然后每个二级目录有2个，三级目录有3个	
def sanjicaidan():
	print("1 2 3 ")
	shuru=raw_input("请输入一个一级目录：")
	if shuru=="1":
		print("1.1,1.2,1.3")
		shuru2=raw_input("please two :")
		if shuru2=="1.1":
			print("1.1.1,1.1.2,1.1.3")
			shuru3=raw_input("please three:")
			if shuru3=="1.1.1":
				print("shi 1.1.1")
				if shuru3=="1.1.2":
					print("shi 1.1.2")
		if shuru2=="1.2":
			print("1.2.1,1.2.2,1.2.3")
			shuru3=raw_input("please three:")
			if shuru3=="1.2.1":
				print("shi 1.2.1")
		if shuru2=="1.3":
			print("1.3.1,1.3.2,1.3.3")
	if shuru=="2":
		print("2.1,.2.2,2.3")
		shuru2=raw_input("two :")
		if shuru2=="2.1":
			print("2.1.1,2.1.2,2.1.3")
			shuru3=raw_input("three:")
			if shuru3=="2.1.1":
				print("shi 2.1.1")
#总结下用if 的方法貌似是可以的，然而这么写下去感觉要累死
#也就是说，数据量一大这么写下去必然要废掉，因为这个有局限性，并且比较低效，尝试下别的方法
#尝试使用字典与列表的方法
#{"1":["1.1","1.2","1.3"]}
#{"1.1":["1.1.1","1.1.2","1.1.3"]}
def sanjishuru():
	test1={"1":["1.1","1.2","1.3"]}
	test2={"1.1":["1.1.1","1.1.2","1.1.3"]}
	if test1.keys=="1":
		print(test1.values)
		xuanze=raw_input("na yige :")
		if xuanze=="1.1":
			print(test2.values)
			xuanze2=raw_input("xuanze:")
			if xuanze2=="1.1.1":
				print("shi 1.1.1")
#这里给我的感觉就是用keys和value剩下了不少东西，但是还是感觉不完美

#总结：
#看第二天的作业讲解，改进下


#重要的一点是我犯的错误：
#忘记if冒号
#忘记def括号				
#所以还得多练
#还有一点就是：先造构架，先简单，先一条，然后在细节，在复杂，在两条。
			
		
