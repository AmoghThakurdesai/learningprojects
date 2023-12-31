%macro IO 4
mov rax,%1
mov rdi,%2
mov rsi,%3
mov rdx,%4
syscall
%endmacro

; -----------------------------------------------

section .data

msg1: db "enter choice (1. +, 2. -, 3. *, 4. /, 5. Exit): ", 0xA
len1 equ $-msg1 

msg2: db "The 2 numbers are: ", 0xA
len2 equ $-msg2

n1: dq 15h
n2: dq 5h

rem_msg: db "Remainder is: ", 0xA
len_rem equ $-rem_msg

quo_msg: db "Quotient is: ", 0xA
len_quo equ $-quo_msg

m_qou db "qoutient is "
m_qou_l equ $-m_qou

m_rem db "remainder is "
m_rem_l equ $-m_rem

; -----------------------------------------------

section .bss

choice resb 2
ans resb 16

; -----------------------------------------------
section .text

global _start
_start:

IO 1,1,msg1,len1
IO 0,0,choice,2

cmp byte[choice], 34H
JE divlbl
cmp byte[choice], 33H
JE mullbl
cmp byte[choice],32H
JE sublbl
cmp byte[choice],31H
JE addlbl

sublbl:
mov rax, [n1]
mov rbx, [n2]
sub rax, rbx
call HtoA
JMP exit

addlbl:
mov rax, [n1]
mov rbx, [n2]
add rax, rbx
call HtoA
JMP exit

mullbl:
xor rdx, rdx
mov rax, [n1]
mov rbx, [n2]
mul rbx
push rax
mov rax, rdx
xor rdx, rdx
call HtoA
pop rax
call HtoA
JMP exit

divlbl:
xor rdx, rdx
mov rax, qword[n1]
mov ebx, dword[n2]
div ebx
push rax
mov rax, rdx
IO 1,1,rem_msg,len_rem
call HtoA
pop rax
IO 1,1,quo_msg,len_quo
call HtoA
JMP exit


exit:
mov rax, 60		
mov rdi, 00
syscall

; -----------------------------------------------

HtoA:
mov rsi, ans        	
mov rcx, 16h        	

hextoascii:
rol  rax  , 04       	          
mov  rdx  , rax       	
and  rdx  , 0Fh      	
cmp  rdx  , 09h      	
jbe  copydigit      	
add  rdx  , 07h      	

copydigit:
add  rdx , 30h      
mov  [rsi]  ,  rdx   	
inc  rsi            	
dec  rcx            	
jnz  hextoascii

IO 1,1,ans,16
ret
