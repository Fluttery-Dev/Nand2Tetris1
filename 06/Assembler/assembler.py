
# COMP command mappping in c instruction

mp_cmp = {
    "0":"101010",
    '1' : '111111',
    '-1' : '111010',
    'D' : '001100',
    'A' : '110000',
    '!D' : '001101',
    '!A' : '110001',
    '-D' : '001111',
    '-A' : '110011',
    'D+1' : '011111',
    'A+1' : '110111',
    'D-1' : '001110',
    'A-1' : '110010',
    'D+A' : '000010',
    'D-A' : '010011',
    'A-D' : '000111',
    'D&A' : '000000',
    'D|A' : '010101',
     "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }

# DEST command mappping in c instruction

mp_dst = {
    'null' : '000',
    'M' : '001',
    'D' : '010',
    'MD' : '011',
    'A' : '100',
    'AM': '101',
    'AD' : '110',
    'AMD' : '111'
    }

# JUMP command mappping in c instruction

mp_jmp = {
    'null':'000',
    'JGT': '001',
    'JEQ':'010',
    'JGE': '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111'
}

# Variables map

mp  = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

for i in range(16):
    x = 'R'+ str(i)
    mp[x] = i
# Converter class to convert commands to binary

class converter:
    
    def comp(self,ins):
        code = ""

        if 'M' not in ins:
            code += '0'
    
        code += mp_cmp[ins]
    
        return code
    
    def dest(self,ins):
        return mp_dst[ins]
        
    def jump(self,ins):
        return mp_jmp[ins]
        

#Parses the commands and calls converter to convert them
varcnt = 16
class assembler:

    def instA(self,ins):
        # print(ins)
        global varcnt
        global mp
        if ins[1].isalpha():
            t= ins[1:]
            if t not in mp.keys():
                mp[t] = varcnt
                varcnt+=1
            ins = ins.replace(t,str(mp[t]))
        
        return format(int(ins[1:]), '016b')

    def instC(self,ins):
    #    print(ins)
        i=0
        for x in ins:
            if(x=='='):
                break
            else:
                i+=1
        
        dst = ins[:i]
        cmp = ins[i+1:]
        i = 0
        for x in cmp:
            if x==';':
                break
            else: i+=1

        jmp = cmp[i+1:]
        cmp = cmp[:i] 

        cd = converter()
        code="111"
        code += cd.comp(cmp)
        code += cd.dest(dst)
        code += cd.jump(jmp)

        return code


# strips out all the blank spaces and comments

def rem(str):
    str = str.replace(' ','')
    str = str.replace('\n','')
    if (str.rfind('//') != -1):
        str = str[0:str.rfind('//')]
    return str    

#normalise c instruction

def normaliseC(str):
    if '=' not in str:
        str = 'null='+str
    if ';' not in str:
        str = str+";null"
    return str


def firstPass():

    rr = open(r"E:\nand2tetris\projects\06\pong\PongL.asm", "r")
    wr = open(r"E:\nand2tetris\projects\06\pong\PongT.asm", "w")
    wr.truncate(0)
    lineNum = 0

    for line in rr:
        line = rem(line)  
        if(line == ""):
            continue
        
        if line[0] == '(':
            x = line[1:-1]
            mp[x] = lineNum
            continue
            
        if line[0] != '@':
            line = normaliseC(line)
        
        wr.write(line)
        wr.write('\n')                           
        lineNum+=1
    
    rr.close()
    wr.close()


#the fukin main function

def main():
    firstPass()
    asm = assembler()
    rr = open(r"E:\nand2tetris\projects\06\pong\PongT.asm")
    wr = open(r"E:\nand2tetris\projects\06\pong\outL.hack",'w')
    
    for line in rr:
        line = line.strip()

        if(line[0] == '@'):
            wr.write(asm.instA(line))
            wr.write("\n")
        else:
            wr.write(asm.instC(line))
            wr.write("\n")
    
    rr.close()
    wr.close()

main()
