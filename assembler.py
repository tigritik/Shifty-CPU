test = '''LDR a b c
STR a d b
ADD b a d'''

symbols = {
    "ldr" : "00",
    "str" : "01",
    "add" : "10",
    "sub" : "11",
    "a" : "00",
    "b" : "01",
    "c" : "10",
    "d" : "11"
}

def assemble(file_name):
    out = ""
    
    instructions = test.split('\n')
    for instruction in instructions:
        
    return out
    with open(file_name, mode='r') as f:
        for instruction in f:
            instruction = instruction.lower()
            cmd, r1, r2, arg3 = instruction.split(' ')
            if cmd == 'mov':
                cmd = 'add'
                arg3 = r2
                r2 = 'd'
                
            use_reg3 = False
            try:
                arg3 = int(arg3)
            except:
                use_reg3 = True

            if use_reg3:
                out += (symbols[cmd] + symbols[r1] + symbols[r2] + symbols[r3] + '1' + '0'*7)
            else:
                immediate_size = 7
                if arg3 < 0:
                    imm = f"{-1*arg3:0b}"
                    imm = '1'*(immediate_size - len(imm)) + imm
                else:
                    imm = f"{arg3:0{immediate_size}b}"
                
                out += (symbols[cmd] + symbols[r1] + symbols[r2] + '00' + '0' + imm)
    
def binary_to_hex(bin_str):
    instruction_byte_length = 2
    instruction_bit_length = 8*instruction_byte_length
    for i in range(0, len(bin_str), instruction_bit_length):
        print(hex(int(bin_str[i:i+instruction_bit_length], base=2)))
        
binary_to_hex(assemble(""))
