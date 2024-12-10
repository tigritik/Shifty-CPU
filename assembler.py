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
        instruction = instruction.lower()
        cmd, r1, r2, r3 = instruction.split(' ')
        out += (symbols[cmd] + symbols[r1] + symbols[r2] + symbols[r3])
    return out
    #with open(file_name, mode='r'):
    
def binary_to_hex(bin_str):
    instruction_byte_length = 1
    instruction_bit_length = 8*instruction_byte_length
    for i in range(0, len(bin_str), instruction_bit_length):
        print(hex(int(bin_str[i:i+instruction_bit_length], base=2)))
        
binary_to_hex(assemble(""))
