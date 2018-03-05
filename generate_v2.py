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

#warm up instructions 
for i in range(0, 10):
   file_object.write('__asm {NOP};\n')

#read operands 
op_file = open('op_file.txt')
op_list = op_file.readlines()


#generate test instructions (MUL in this example)  
for i in range(0, len(op_list)):
   index1 = randint(0,10)
   index2 = randint(0,10)
   index3 = randint(0,10)
   op1, op2 = op_list[i].split()[0], op_list[i].split()[1]
   #generate MUL instructions with random registers 
   file_object.write('__asm {MUL r' + str(index1) + ', r' + str(index2) + ', r' + str(index3) + '};\n')   

#cooling down instructions
for i in range(0, 10): 
   file_object.write('__asm {NOP};\n')   
   
file_object.write('return 0;\n')
file_object.write('}')
