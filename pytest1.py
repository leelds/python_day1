#encoding:UTF-8
#��д��¼����
#��֤�ɹ�����ʾ��ӭ��Ϣ
#����������κ�����
def denglu():                                     #д��� û��()
	pass_world=raw_input("please input your passworld:")
	if pass_world=="12.34":
		print("yes,the passworld is OK ,you can do it now")
	if pass_world!="12.34":                     #��������﷨��Ч   ����һ��ð��
		print("please try again")
		count=3
		count=count-1
		if count==0:
			print("you have no time")
			#break
		#break

#������1����һ��Ŀ¼1.1�������Ŀ¼1.1.1��������Ŀ¼
#����д1��2��3����һ��Ŀ¼��Ȼ��ÿ������Ŀ¼��2��������Ŀ¼��3��	
def sanjicaidan():
	print("1 2 3 ")
	shuru=raw_input("������һ��һ��Ŀ¼��")
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
#�ܽ�����if �ķ���ò���ǿ��Եģ�Ȼ����ôд��ȥ�о�Ҫ����
#Ҳ����˵��������һ����ôд��ȥ��ȻҪ�ϵ�����Ϊ����о����ԣ����ұȽϵ�Ч�������±�ķ���
#����ʹ���ֵ����б�ķ���
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
#������ҵĸо�������keys��valueʣ���˲��ٶ��������ǻ��Ǹо�������

#�ܽ᣺
#���ڶ������ҵ���⣬�Ľ���


#��Ҫ��һ�����ҷ��Ĵ���
#����ifð��
#����def����				
#���Ի��ö���
#����һ����ǣ����칹�ܣ��ȼ򵥣���һ����Ȼ����ϸ�ڣ��ڸ��ӣ���������
			
		
