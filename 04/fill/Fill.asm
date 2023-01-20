// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//intitialise A with no of registers to blacken/whiten
@8192
D=A

@n
M=D



//Infinite LOOP

(LOOP)

//Get keyboard inoput 
@KBD
D=M

//check if pressed
@PRESSED
D;JGT

//if not pressed set color to 0 and call fillcolor
@color
M=0
@FILLCOLOR
0;JMP

//if pressed set color to -1 and call fillcolor
(PRESSED)
@color
M=-1

@FILLCOLOR
0;JMP



//sets n registers on screen to color
(FILLCOLOR)
//get screen coordinates
@SCREEN
D=A
@temp
M=D

@i
M=0

//fill the registers
(FILL)
@i
D=M

@n
D=M-D
@LOOP
D;JEQ

@color
D=M

@temp
M=M+1
A=M-1
M=D

@i
M=M+1
@FILL
0;JMP

@LOOP
0;JMP
