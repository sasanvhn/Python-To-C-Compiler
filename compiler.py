import re
import os
import time
try:
    from colorama import Fore
except:
    os.system('pip install colorama')

logo1=" ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗██╗     ███████╗██████╗ "
logo2="██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗"
logo3="██║     ██║   ██║██╔████╔██║██████╔╝██║██║     █████╗  ██████╔╝"
logo4="██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║██║     ██╔══╝  ██╔══██╗"
logo5="╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║███████╗███████╗██║  ██║"
logo6=" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝"
print('')
print(Fore.RED+logo1)
time.sleep(0.1)
print(Fore.RED+logo2)
time.sleep(0.1)
print(Fore.RED+logo3)
time.sleep(0.1)
print(Fore.RED+logo4)
time.sleep(0.1)
print(Fore.RED+logo5)
time.sleep(0.1)
print(Fore.RED+logo6)
time.sleep(0.1)

symbol_key=[]
op_list=[]
x=[]
all_line_true=[]
def lexical_analysis(index,code,file_py):
    global x
    # all pattern

    # pattern for symbol key
    t_for=r'for'
    t_while=r'while'
    t_if=r'if'
    t_elif=r'elif'
    t_else=r'else'
    t_break=r'break'
    t_continue=r'continue'
    t_return=r'return'
    t_try=r'try'
    t_except=r'except'
    t_in=r'in'
    t_range=r'range'
    t_print=r'print'
    t_input=r'input'

    # pattern for variable
    t_variable= r'/s[a-zA-Z0-9]*=[a-zA-Z0-9]*/s'
    # pattern for operator
    t_equal=r'=='
    t_equal_not=r'!='
    t_more=r'>'
    t_less=r'<'
    t_more_equal=r'>='
    t_less_equal=r'<='
    # t_and=r'and'
    # t_or=r'or'
    # t_not=r'not'

    t_plus_equal=r'+='
    t_mines_equal=r'-='
    t_multi_equal=r'*='
    t_dev_equal=r'/='

    t_plus=r'+'
    t_mines=r'-'
    t_multi=r'*'
    t_dev=r'/'
    t_bagi=r'%'

    


    token_key=[t_for,t_while,t_if,t_elif,t_else,t_break,t_continue
    ,t_return,t_try,t_except,t_in,t_range,t_print,t_input]

    token_op=[
        t_equal,
        t_equal_not,
        t_more,
        t_less,
        t_more_equal,
        t_less_equal,
        # t_and,
        # t_or,
        # t_not,
        t_plus_equal,
        t_mines_equal,
        t_multi_equal,
        t_dev_equal,
        t_plus,
        t_mines,
        t_multi,
        t_dev,
        t_bagi
    ]
    
    # get all key and append to list
    for tk in token_key:
        if tk in code:
            if tk not in symbol_key:
               symbol_key.append(tk)

    # get op in code
    for tk in token_op:
        if tk in code:
            if tk not in op_list  :
                op_list.append(tk)

    # get variable in code
    # a=12 a+=1
    pat=r' [a-zA-Z]{1} |^[a-zA-Z][a-zA-Z0-9]*=[0-9a-zA-Z"\']*'
    x=re.findall(pat,file_py,re.MULTILINE)
    

def show_key():
    global x
    print(Fore.CYAN+'------------------------------')
    print(Fore.YELLOW+'all key in python file : '.upper()+Fore.GREEN)
    for key in symbol_key:
        print(key)

    print(Fore.CYAN+'------------------------------')
    print(Fore.YELLOW+'all operation in python file :'.upper()+Fore.GREEN)
    for op in op_list:
        print(op)

    print(Fore.CYAN+'------------------------------')
    print(Fore.YELLOW+'all of variable'.upper()+Fore.GREEN)
    for index,item in enumerate(x,start=1):
        print(index,' : ',item)  
    print(Fore.CYAN+'------------------------------')    
     
counter=1 
def syntax_analysis(index,everylinecode,allcode):
    global counter
    # pattern
    # for i in range(1,100):
    pat_for=r'\s*for \s*[a-zA-Z]* in range\s*[(][0-9]*,[0-9]*[)]\s*:'
    # while i<10:
    pat_while=r'\s*while \s*[a-zA-Z0-9_]*\s*[==|!=|>|<|>=|<=]*\s*[0-9a-zA-Z\'"]*\s*:'
    # if i==0:
    pat_if1=r'\s*^if \s*[a-zA-Z0-9_]*\s*[==|!=|>|<|>=|<=]*[0-9a-zA-Z"\']*\s*:'
    # if i%2==0:
    pat_if2=r'^\s*if \s*[a-zA-Z0-9_]*\s*[%]\s*[0-9]*\s*[==|!=|>|<|>=|<=]*\s*[0-9]*\s*:'
    # elif i==4:
    pat_elif1=r'\s*elif \s*[a-zA-Z0-9_]*\s*[==|!=|>|<|>=|<=]*[0-9a-zA-Z"\']*\s*:'
    # elif i%2!=0:
    pat_elif2=r'^\s*elif \s*[a-zA-Z0-9_]*\s*[%]\s*[0-9]*\s*[==|!=|>|<|>=|<=]*\s*[0-9]*\s*:'
    # else:
    pat_else=r'\s*else\s*:'
    # print('hi')
    pat_print1=r'\s*print\s*[(]\s*[\'|"]\s*[a-zA-Z0-9_ ]*\s*[\'|"]\s*[)]'
    # print(i)      
    pat_print2=r'\s*print\s*[(]\s*[a-zA-Z0-9_]*\s*[)]'
    # a=a+1
    pat_op=r'[a-zA-Z0-9_]*\s*=\s*[a-zA-Z0-9_]*\s*[+|-|*|/]\s*[0-9a-zA-Z_"\']*'
    # a=1 name='mohsen'
    pat_define_var=r'\s*^[a-zA-Z][a-zA-Z0-9_]*\s*=\s*["0-9a-zA-Z_\'"]*'

    token=[pat_for,pat_while,pat_if1,pat_if2,pat_elif1,pat_elif2,pat_else,pat_print1,pat_print2,pat_op,pat_define_var]
    all_syntax=[]
    for tk in token:
        compire=re.findall(tk,everylinecode,re.MULTILINE)
        compire=''.join(compire)
        if compire=='' or compire==' ' or compire==None:
            continue
        all_syntax.append(compire)
    # print(all_syntax)
    if len(all_syntax)!=1:
        print(Fore.RED+'you have error on line : '.upper(),index,'you write : '.upper()+everylinecode)   
        print(Fore.WHITE+'')
        quit ()
    else:
        print(Fore.GREEN+'code in line '.upper(),index,' is ok'.upper())
        counter+=1
        if counter==len(allcode):
            compile_to_c()
            pass
        
        

    # print(all_line_syntax)
c_code="""
#include<stdio.h>\n
void main()
{}
"""
def compile_to_c():
    global c_code
    file=open('p.txt','r').read().split('\n')
    
    # define var
    if_list=[]

    # define pattern
    # python pattern
    pat_while_py=r'\s*[a-zA-Z0-9_]*\s*[==|>|<|>=|<=|!=]*\s*[a-zA-Z0-9"\']*\s*'
    pat_print_py=r'["|\'][ a-zA-Z0-9_]*["|\']\s*|\s*[(][a-zA-Z0-9_]*[)]'
    pat_for_py=r'\s*[0-9]*\s*,\s*[0-9]*\s*'
    pat_if_py=r'\s*[a-zA-Z0-9_%]*\s*[==|!=|>|<|>=|<=]*\s*[a-zA-Z0-9_\'"]*\s*'
    # pat_if1=r'\s*^if \s*[a-zA-Z0-9_]*\s*[==|!=|>|<|>=|<=]*[0-9a-zA-Z"\']*\s*:'
    pat_op_py=r'[a-zA-Z0-9_]*\s*=\s*[a-zA-Z0-9_]*\s*[+|-|*|/]\s*[0-9a-zA-Z_"\']*\s*'
    # a=1 name='mohsen'
    pat_var_py=r'\s*^[a-zA-Z][a-zA-Z0-9_]*\s*=\s*["0-9a-zA-Z_\'"]*\s*'
    # c pattern
    pat_for_c='for(int i={};i<{};i++)'
    pat_while_c='while ({})'
    pat_print_c='printf({})'
    pat_if_c='if({})'
    pat_else_if_c='else if({})'
    pat_else_c='else'
    print_=''

    # help c
    for_=''
    if_=''
    elif_=''
    else_=''
    print_=[]

    for f in file[0:8]:
        if 'for' in f:
            x=re.findall(pat_for_py,f,re.MULTILINE)
            x=''.join(x)
            x=x.split(',')
            for_=pat_for_c.format(str(x[0]),str(x[1]))+'\n{}'
            # print(for_)
        if 'if' in f and 'elif' not in f:
            x=re.findall(pat_if_py,f,re.MULTILINE)
            x=''.join(x)
            x=x.split('if')
            if len(x)>1:
                if_=pat_if_c.format(str(x[1]))+'\n'+"{}"
                # print(if_)
        
        if 'elif' in f:
            x=re.findall(pat_if_py,f,re.MULTILINE)
            x=''.join(x)
            x=x.split('elif')
            # print(x)
            if len(x)>1:
                elif_=pat_else_if_c.format(str(x[1]))+'\n'+"{}"
                # print(elif_)

        if 'else' in f:
            else_='else'+"\n"+"{}"      
            # print(else_)  

        if  'print' in f :
            x=re.findall(pat_print_py,f,re.MULTILINE)
            x=''.join(x)
            print_.append(pat_print_c.format(str(x))+';')
            # print(print_)

    char=''
    list_=[if_,elif_,else_]
    if len(list_)==len(print_):
        char+=list_[0].format('{'+'\n'+print_[0]+"\n"+"}")+'\n'
        char+=list_[1].format('{'+'\n'+print_[1]+"\n"+"}")+'\n'
        char+=list_[2].format('{'+'\n'+print_[2]+"\n"+"}")+'\n'

    # print(char)

    char=for_.format('{'+'\n'+char+"\n"+"}"+'\n')
    # print(for_)


    while_=''
    pr_=''
            
    for i,f in enumerate(file[7:]):
        if i==0:
            char+='int '+f+';'+'\n'
        elif i==1:
            char+='int '+f+';'+'\n'
        elif i==2:
            x=re.findall(pat_while_py,f,re.MULTILINE)
            x=''.join(x)
            x=x.split(' ')
            # print(x)
            if len(x)>1:
                while_=pat_while_c.format(str(x[1])+str(x[2])+str(x[3]))+"\n"+"{"+"\n"
                char+=while_
        elif i==3:
            char+=f+";"+"\n"
        elif i==4:
            char+=f+";"+"\n"+"}"+'\n'
        elif i==5:
            x=re.findall(pat_print_py,f,re.MULTILINE)
            x=''.join(x)
            if x[0]=='(' and x[-1]==')':
                x=x[1:-1]
            pr_=pat_print_c.format(str(x))+';'
            char+=pr_
            
        

    
        # print(char)
    c_code=c_code.format("{"+"\n"+char+"\n"+"}")
    # print(c_code)

    file2=open('c.txt','w')
    file2.write(c_code)

def remove_space(string):
    sum=''
    for i in range(len(string)):
        if string[i]==' ':
            continue
        sum=string[i:]
        break
    return sum            
    

def compiler():
    file_py=open('p.txt','r').read()
    # print(file_py)
    file_py_sp=file_py.split('\n')
    # print(len(file_py_sp))
    # give code to lexical analyzer
    for index,code_line in enumerate(file_py_sp,start=1):
        lexical_analysis(index,code_line,file_py)
    show_key()  
    # give code to syntax analyzer  
    for index,code_line in enumerate(file_py_sp,start=1):
        # if index==len(file_py_sp):
        #     break
        # print(index,code_line)
        syntax_analysis(index,code_line,file_py_sp)
        
    



if __name__=="__main__":
    compiler()
    
  
