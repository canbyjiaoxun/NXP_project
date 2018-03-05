from random import *
import os 
import shutil 

file_object = open ('main.c', 'w')
file_object.write('#include "LPC11xx.h"\n')
file_object.write('#include "loctypes.h"\n')
file_object.write('#include <stdio.h>\n')
file_object.write('#include <stdlib.h>\n')
file_object.write('#include <math.h>\n')
file_object.write('#include "arm_math.h"\n')

file_object.write('\n')


file_object.write('INT32 main (void) {\n')
file_object.write('UINT32 add = 0;\n')
file_object.write('UINT32 add1 = 100;\n')
file_object.write('UINT32 add2 = 200;\n')
file_object.write('UINT32 a = 1;\n')
for i in range(0, 7):
	file_object.write('__asm {NOP};\n')

operand1 = 100
operand2 = 200
operand3 = 300

mode = raw_input('What is the mode, random, increment or matrix')
if mode == 'increment':
   step1 = raw_input('What is the step size for operand1')
   step2 = raw_input('What is the step size for operand2')
   #step3 = raw_input('What is the step size for operand3')

   for i in range(0,1000):
		file_object.write('__asm {ORR add,' + str(operand1) + ',' + str(operand2) + '};\n')
		#file_object.write('__asm {MLA add,' + str(operand1) + ',' + str(operand2) + '};\n')
	  #  file_object.write('__asm {MLA add,add1,' + str(operand2) + '};\n')
	  # file_object.write('__asm {MOV r0,#0xe740};\n')
	  # if step == 0:
	   #file_object.write('__asm {MOV };\n')
		operand1 = operand1 + int(step1)
		operand2 = operand2 + int(step2)
		#operand3 = operand3 + int(step3)
elif mode == "random":
   for i in range(0, 1000):
		file_object.write('__asm {ORR add,' + str(operand1) + ',' + str(operand2) + '};\n')
		#file_object.write('__asm {NOP};\n')
		#operand1 = randint(0,1000)
		operand2 = randint(0,1000)
		#operand3 = randint(0,4000)
elif mode == "matrix":
    shutil.copy2('main_matrix.c', 'main.c')
else:
   print 'wrong mode, please input again'

for i in range(0, 7):
	file_object.write('__asm {NOP};\n')   
   
file_object.write('return 0;\n')
file_object.write('}')
