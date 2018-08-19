import os, pathlib

os.chdir('./test-mkdir/testmkdir')
print(os.getcwd())
print(os.listdir())
	
#for m in range(0, 101, 10):
	#print("%02d" % m, end = " ")
	#print('%03d' % m)
	#os.makedirs('./testmkdir/sample/my/#03d_test_20180818' % m)

for m in range(1, 11):
	pathlib.Path('%02d_test-file_20180818c.py' % m).touch()
