symbols = {
    "ldr" : "00",
    "str" : "01",
    "add" : "10",
    "sub" : "11",
    "a" : "11",
    "b" : "10",
    "c" : "01",
    "d" : "00"
}

def assemble(file_name):
    out = ""
    data_out = ""
    
    with open(file_name, mode='r') as f:
        text = f.read().split('data\n')
        data = ""
        if len(text) > 1:
            data = text[1].strip()
        text = text[0].strip()
        
    for instruction in text.split('\n'):
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
    
    for line in data.split('\n'):
        type, val = line.split(' ')
        if type.lower() == 'string':
            for c in val:
                data_out += f"{ord(c):08b}"[-8:]
            data_out += '0'*8
        else:
            if type.lower() == 'char':
                val = str(ord(val))
                length = 8
            elif type.lower() == 'byte':
                length = 8
            elif type.lower() == 'word':
                length = 16
            elif type.lower() == 'dword':
                length = 32
            elif type.lower() == 'quad':
                length = 64
            else:
                raise ValueError(f"Unknown data type {type}")
            data_out += f"{int(val):0{length}b}"[-1*length:]

    return out, data_out
    
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
                current_instruction = f" {current_instruction:0{2*instruction_byte_length}x}"
                f.write(current_instruction)
                current_index += instruction_bit_length
            f.write('\n')

def data_to_hex(data_in):
    byte = 8
    with open("a.data", mode='w') as f:
        f.write("v3.0 hex words addressed\n")
        data_in = data_in.ljust(256*byte, '0')
        
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        current_index = 0
        for i in range( len(hex_digits) ):
            f.write(hex_digits[i] + '0:')
            for j in range(byte):
                current_data = data_in[current_index : current_index + byte]
                current_data = int(current_data, base=2)
                current_data = f" {current_data:02x}"
                f.write(current_data)
                current_index += byte
            f.write('\n')
            
text, data = assemble("sample_program.txt")
binary_to_hex(text)
data_to_hex(data)
