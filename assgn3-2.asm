%macro print 2
    mov rax, 01           
    mov rdi, 01           
    mov rsi, %1          
    mov rdx, %2          
    Syscall
%endmacro

%macro hex_ascii 2
    mov rcx, 02          
    mov rbp, %1            
    mov bl, %2             

    %%label1:              
    rol bl, 04             
    mov dl, bl             
    and dl, 0Fh            
    cmp dl, 09h            
    jbe %%label2
    add dl, 07h            
    
    %%label2:              
    add dl, 30h        
    mov [rbp], dl         
    inc rbp                
    dec rcx               
    jnz %%label1           
%endmacro

section .data
arr db 11h ,  12h , 15h , 20h , 10h             
M1 db "The given array is....." , 10
L1 equ $-M1
M2 db 10 , "The largest no in array is...." , 10
L2 equ $-M2

section .bss
ans resb 2                   
counter resb 1               

section .text
global _start
_start:
    print M1,L1

    mov byte[counter], 05         
    mov rsi, arr                  

    label3:                       
    mov al, [rsi]                 
    push rsi                      
    hex_ascii ans,al              
    print ans,2                   
    mov byte[ans] , 10            
    print ans,1                   
    pop rsi                       
    inc rsi                       
    dec byte[counter]             
    jnz label3                    
    
    mov rsi,  arr                 
    mov al, 00h                   
    mov byte[counter] ,04         
    
    start_compare:                    
    cmp [rsi], al                 
    jbe ahead                     
    mov al, [rsi]                 
    
    ahead:                       
    inc rsi                      
    dec byte[counter]             
    jnz start_compare             
    
    print M2,L2 
    hex_ascii ans,al              
    print ans,2                 
    
    mov rax, 60                   
    mov rdx, 0                   
    Syscall
