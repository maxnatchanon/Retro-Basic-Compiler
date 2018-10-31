# Retro Basic Compiler
This project is a part of 2110316 Programming Languages Principles at Chulalongkorn University.

**Task :**  
Write a compiler to translate the source of Retro Basic to the B-code.
The compiler must be able to check the grammar and report the error if input file is incorrect.

**Grammar :**   
```
pgm := line pgm | EOF  
line := line_num stmt  
stmt := asgmnt | if | print | goto | stop  
asgmnt := id = exp  
exp := term + term | term - term  | term
term := id | const  
if := IF cond line_num  
cond := term < term | term = term  
print := PRINT id  
goto := GOTO line_num  
stop := STOP  
```
  
**Example :**  
```
// Input
10 A = 1  
20 IF 10 < A 60   
30 PRINT A  
40 A = A + 1  
50 GOTO 20  
60 STOP
```

```
// Output
10 10 11 1 17 4 12 1  
10 20 11 19 17 4 12 0  
10 30 13 0 12 10 17 3 11 1 14 70  
10 40 11 19 17 4 11 19 17 1 11 1  
10 50 11 1 17 4 11 1 17 1 12 1  
10 60 14 30  
10 70 15 0 11 19  
10 80 16 0 
```
 
 **How to run :**  
 1. Put your input code in *input.txt*
 2. Run *main_compiler.py*
 3. The output will be in *output.txt* 
 
 *Full project description [here](https://www.cp.eng.chula.ac.th/~piak/teaching/prolang/2018/retro-basic.htm)*
 *Project report is available in repo (Project_Report.pdf)*
