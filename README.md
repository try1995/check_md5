# check_md5
检查md5的小工具，支持文件夹，指定检查的文件类型，指定不检查目录


使用平台：windows,linux
使用方法：命令行方式使用
window可以用pyinstaller -F check_md5.py打包成exe文件使用。或者安装Python3和argparse库，将下面的check_md5.exe换成check_md5.py直接使用

cd 到check_md5.exe的路径，或者加到环境变量里面
check_md5.exe -h   查看帮助
 -o 输入路径或者文件，（必输）
-c 输入路径或者文件， 
-s 输入保存的文件，如 -s check.txt会将比对结果保存
-t 限定匹配文件格式，如 -t lib 则只匹配lib文件，多个用英文逗号分割 -t lib,dll
-e 排除不匹配的文件夹，如果日志文件夹 -e log ，多个文件 -e log,abpy,少儿不宜

注意：
1.路径支持中文，文件中如果有空格，必须使用""将路径引起来，否则会导致命令行报错
例如 a big boy.py 使用"a big boy.py"
2.check_md5.exe文件最好不要和要匹配的文件在一个目录里面
3.支持相对路径

多种比对方式示例：
1.计算单个文件的md5:
check_md5.exe -o file_path/myfile.py
这种情况下 -s,-t,-e无效

2. 计算单个文件夹，并保存md5结果（只有这种情况-s命令有效）
check_md5.exe -o file_path -s check.txt

3. 比对文件和文件的md5一致性
	check_md5.exe -o a.py -c b.py 
这种情况下 -s,-t,-e无效

4. 比对文件和文件的md5一致性，不检测log文件夹
	check_md5.exe -o  path_a -c path_b -e log
	打印出以path_a为标准，path_b中缺失和md5不匹配的文件夹和md5
这种情况下 -s无效

5.比较文件夹和2里面的保存md5结果进行比对（一般不在同一个机器的情况）
	check_md5.exe -o path_a -c check.txt
打印出以check.txt为标准，path_a中缺失和md5不匹配的文件夹和md5
这种情况下 -s,-t,-e无效

