import sys

def main():

    debug = False
    stop = False

    if len(sys.argv) > 1:

        mem_size = 10
        mem = [0] * mem_size
        address = 0
        pointer = 0
        limit = sys.maxint
        # read the command options
        for i in range(1,len(sys.argv)-1):
            print sys.argv[i]
            if sys.argv[i] == '-d':
                debug = True
            elif sys.argv[i] == '-s':
                stop = True
                print '\n'*40
            elif sys.argv[i] == '-l':
                n = int(sys.argv[i+1])
                if n > 1 and n <= 32:
                    limit = pow(2, n) - 1
            elif sys.argv[i] == '-m':
                n = int(sys.argv[i+1])
                if n > 1 and n <= 100000:
                    mem_size = n

        file = open(sys.argv[-1])
        source = file.read()

        while(pointer < len(source)):

            #debug informations
            if(debug or stop):
                print source
                print 'len\t', len(source)
                print 'pointer\t', pointer
                print 'instr\t', source[pointer]
                print 'address\t', address
                print 'value\t', mem[address]
                print 'limit\t', limit
                print 'cells\t', mem_size
                print mem

            if(stop):
                raw_input()

            if source[pointer] == '>':
                address += 1
                if(address >= mem_size):
                    address = 0
                pointer+=1

            elif source[pointer] == '<':
                address -= 1
                if(address < 0 ):
                    address = mem_size - 1
                pointer+=1

            elif source[pointer] == '+':
                #if abs(mem[address] < 255):
                mem[address] += 1
                pointer+=1

            elif source[pointer] == '-':
                #if abs(mem[address]) < 255:
                mem[address] -= 1
                pointer+=1

            elif source[pointer] == '.':
                sys.stdout.write(unichr(mem[address]))
                pointer+=1

            elif source[pointer] == ',':
                user_input = raw_input('input: ')
                try:
                    mem[address] = int(user_input)
                except ValueError, e:
                    mem[address] = ord(user_input)
                pointer+=1

            elif source[pointer] == '[':
                count = 1
                if mem[address] == 0:
                    while(source[pointer-1] != ']' or count > 0):
                        pointer+=1
                        if source[pointer] == '[':
                            count+=1
                        elif count > 0 and source[pointer] == ']':
                            count-=1
                else:
                    pointer+=1

            elif source[pointer] == ']':
                count = 0
                if mem[address] != 0:
                    while(source[pointer-1] != '[' or count > 0):
                        pointer-=1
                        if source[pointer] == ']':
                            count+=1
                        elif count > 0 and source[pointer] == '[':
                            count-=1
                else:
                    pointer+=1

            elif source[pointer] == '#':
                stop = True
                pointer+=1

            elif source[pointer] == '\n' or source[pointer] == '\t' or source[pointer] == ' ':
                pointer+=1


            else:
                print 'Unexpected char \'', source[pointer], 'at index', pointer
                break
    else:
        print 'python brainfuck.py [options] brainfuck_source_file\n'
        print 'brainfuck interpreter - (C) 2016 Samir Ettali\n'
        print 'a hash (#) in the source file is equivalent to a breakpoint\n'
        print 'options:'
        print '\t-d\tprints the memory at every instruction'
        print '\t-s\tprints the memory and pauses the execution at every instruction'
        print '\t-l [n]\tsets the variable limit at 2^[n]-1'
        print '\t-m [n]\tsets the memory cells number at [n]'


if __name__ == '__main__':
    main()
