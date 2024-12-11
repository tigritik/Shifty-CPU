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
    
    with open(file_name, mode='r') as f:
        for instruction in f:
            instruction = instruction.lower()
            cmd, r1, r2, arg3 = instruction.split(' ')
            arg3 = arg3.strip()
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
                out += (symbols[cmd] + symbols[r1] + symbols[r2] + symbols[arg3] + '1' + '0'*7)
            else:
                immediate_size = 7
                if arg3 < 0:
                    imm = f"{-1*arg3:0b}"
                    imm = '1'*(immediate_size - len(imm)) + imm
                else:
                    imm = f"{arg3:0{immediate_size}b}"
                
                out += (symbols[cmd] + symbols[r1] + symbols[r2] + '00' + '0' + imm)

    return out
    
def binary_to_hex(bin_str):
    instruction_byte_length = 2
    instruction_bit_length = 8*instruction_byte_length
    with open("a.out", mode='w') as f:
        f.write("v3.0 hex words addressed\n")
        bin_str = bin_str.ljust(256*instruction_bit_length, '0')

        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        current_index = 0
        for i in range( len(hex_digits) ):
            f.write(hex_digits[i] + '0:')
            for j in range(16):
                current_instruction = bin_str[current_index : current_index + instruction_bit_length]
                current_instruction = int(current_instruction, base=2)
                if current_instruction < 0:
                    current_instruction = ' ' + '1'*(2*instruction_byte_length - len(current_instruction)) + f"{-1*current_instruction:0x}"
                else:
                    current_instruction = f" {current_instruction:0{2*instruction_byte_length}x}"
                f.write(current_instruction)
                current_index += instruction_bit_length
            f.write('\n')
        
binary_to_hex(assemble("test.txt"))
