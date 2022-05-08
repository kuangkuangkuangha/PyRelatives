386
data segment use16
    buf dw 4ch, 21h, 0fch, 0ffh, 0ah, 0a6h, 0d7h
    num dw $-buf
data ends

stack segment use16 stack
    db 200 dup(0)
stack ends

code segment use16
    assume cs:code, ds:data, ss:stack

begin:
        mov ax, data
        mov ds, ax

        mov cx, num
        xor dx, dx
        xor si, si
        mov bx, 0fch
l:      mov ax, word ptr buf[si]
        cmp ax, bx
        jb l1
        inc dx;
        
l1:     inc si
        inc si
        loop l

return: mov ah, 4ch
        int 21h

code ends
    end start