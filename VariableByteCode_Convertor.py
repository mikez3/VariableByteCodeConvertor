#Convertor with 8 bit blocks
while(True):
    option  = input('Press 1 to convert Int to Variable Byte Code or\nPress 2 to convert Variable Byte Code to Int: ')

    #int to bytecode
    if option == '1':
        #input validation
        while True:
            num = input('Enter a posotive integer: ')
            if (num.isdigit() and int(num) > 0):
                break
            print ('Please enter a valid value')
        
        #conversion
        bits = format(int(num),'b')
        bytecode=''
        bits=bits[::-1]
        for idx,bit in enumerate(bits):
            if (idx % 7 != 0 or idx == 0) and idx!=len(bits):
                bytecode = bit + bytecode
            else:
                if idx==7:
                    bytecode = '1' + bytecode
                else:
                    bytecode = '0' + bytecode
                bytecode = bit+bytecode
        if (len(bytecode) % 8 != 0):
            if (len(bytecode) // 8 ==0):
                bytecode = '1' + '0'*(7-len(bytecode)) + bytecode
            else:
                bytecode = '0'*(8-len(bytecode)%8) + bytecode
        print ('Variable Byte Code:', bytecode)
        # break

    #bytecode to int
    elif option =='2':
        #input validation
        while True:
            bytecode = input('Enter a valid Variable Byte Code: ')
            if (len(bytecode)%8 == 0 and bytecode[-8]== '1'):
                break
            print ('The Variable Byte Code:',bytecode, 'is not valid! Please try again')
        
        #conversion
        bits = ''
        for idx,bit in enumerate(bytecode):
            if (idx%8 != 0 and idx != 0):
                bits += bit
        num = int(bits,2)
        print ('Integer:',num)
        # break
            
    else:
        print('Invalid input. Please try again!')