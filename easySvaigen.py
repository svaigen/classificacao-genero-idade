#!/usr/bin/env python

import sys
import os
import subprocess

# Apenas para contagem de tempo
# Rafael Zottesso - 28/02/15
import timeit
time_start = timeit.default_timer()

if len(sys.argv) <= 1:
	print 'Usage: %s training_file [testing_file]' % sys.argv[0]
	raise SystemExit

# svm, grid, and gnuplot executable

is_win32 = (sys.platform == 'win32')
if not is_win32:
	svmscale_exe = "/home/svaigen/tic-genero-faixaetaria/libsvm-3.22/svm-scale"
	#svmtrain_exe = "../svm-train-gpu"
	svmtrain_exe = "/home/svaigen/tic-genero-faixaetaria/libsvm-3.22/svm-train"
	svmpredict_exe = "/home/svaigen/tic-genero-faixaetaria/libsvm-3.22/svm-predict"
	grid_py = "/home/svaigen/tic-genero-faixaetaria/libsvm-3.22/tools/grid.py"
	gnuplot_exe = "null"
else:
        # example for windows
	svmscale_exe = r"svm-scale.exe"
	svmtrain_exe = r"svm-train.exe"
	svmpredict_exe = r"svm-predict.exe"
	gnuplot_exe = r"pgnuplot.exe"
	grid_py = r"grid.py"



assert os.path.exists(svmscale_exe),"svm-scale executable not found"
assert os.path.exists(svmtrain_exe),"svm-train executable not found"
assert os.path.exists(svmpredict_exe),"svm-predict executable not found"
#assert os.path.exists(gnuplot_exe),"gnuplot executable not found"
assert os.path.exists(grid_py),"grid.py not found"

train_pathname = sys.argv[1]
assert os.path.exists(train_pathname),"training file not found"
file_name = train_pathname.rpartition(".")[0] #file_name = os.path.split(train_pathname)[1]
scaled_file = file_name + ".scale"
model_file = file_name + ".model"
range_file = file_name + ".range"

if len(sys.argv) > 2:
	test_pathname = sys.argv[2]
	file_name = test_pathname.rpartition(".")[0] #os.path.split(test_pathname)[1]
	assert os.path.exists(test_pathname),"testing file not found"
	scaled_test_file = file_name + ".scale"
	predict_test_file = file_name + ".predict"

cmd = "%s -s %s %s > %s" % (svmscale_exe, range_file, train_pathname, scaled_file)
print 'Scaling training data...'
os.system(cmd)

cmd = "python %s -svmtrain %s -gnuplot %s %s" % (grid_py, svmtrain_exe, gnuplot_exe, scaled_file)
print 'Cross validation...'  #raw_input("Press any Key")
dummy, f = os.popen2(cmd)

line = ''
while 1:
	last_line = line
	line = f.readline()
	if not line: break
c,g,rate = map(float,last_line.split())

print 'Best c=%s, g=%s CV rate=%s' % (c,g,rate)

'''
-s svm_type : set type of SVM (default 0)
	0 -- C-SVC		(multi-class classification)
	1 -- nu-SVC		(multi-class classification)
	2 -- one-class SVM	
	3 -- epsilon-SVR	(regression)
	4 -- nu-SVR		(regression)
-t kernel_type : set type of kernel function (default 2)
	0 -- linear: u'*v
	1 -- polynomial: (gamma*u'*v + coef0)^degree
	2 -- radial basis function: exp(-gamma*|u-v|^2)
	3 -- sigmoid: tanh(gamma*u'*v + coef0)
	4 -- precomputed kernel (kernel values in training_set_file)
'''
cmd = "%s -s %s -t %s -c %s -g %s -b 1 %s %s" % (svmtrain_exe,sys.argv[3],sys.argv[4],c,g,scaled_file,model_file)
print 'Training...'
os.popen(cmd)

print( 'Output model: %s' % model_file)
if len(sys.argv) > 2:
	cmd = "%s -r %s %s > %s" % (svmscale_exe, range_file, test_pathname, scaled_test_file)
	print 'Scaling testing data...'
	os.system(cmd)

	cmd = "%s -b 1 %s %s %s" % (svmpredict_exe, scaled_test_file, model_file, predict_test_file)
	print 'Testing...'
	os.system(cmd)

	print 'Output prediction: %s' % predict_test_file
# Contagem de tempo
# Rafael Zottesso - 28/02/15
time_end = timeit.default_timer()
time = time_end - time_start
