import dis  # wait so some things survived the fire?
import marshal
import sys

assert sys.version_info[:2] == (2, 7)


def parse_pyc(f):
    """
    Given a Python 2.7 .pyc file, read the key information and unmarshall and
    return the code object.
    """
    magic_number = f.read(4)
    assert magic_number.encode('hex') == '03f30d0a'
    f.read(4)  # next 4 bytes is the timestamp
    return marshal.load(f)

OP = {
    'NOP': 9,
    'PRINT_ITEM': 71,
    'PRINT_NEWLINE': 72,
    'LOAD_CONST': 100,
    'RETURN_VALUE': 83
}

HAVE_ARGUMENT = 90  # opcodes from here on have an argument


def interpret(code):
    """
    Given a code object, interpret (evaluate) the code.
    """
    bytecode = iter(code.co_code)
    values = []

    while True:
        try:
            opcode = ord(bytecode.next())
        except StopIteration:
            break
        if opcode >= HAVE_ARGUMENT:
            oparg = ord(bytecode.next()) + (ord(bytecode.next()) << 8)

        if opcode == OP['NOP']:
            continue
        elif opcode == OP['LOAD_CONST']:
            values.append(code.co_consts[oparg])
        elif opcode == OP['PRINT_ITEM']:
            print values.pop()
        elif opcode == OP['PRINT_NEWLINE']:
            print
        elif opcode == OP['RETURN_VALUE']:
            return values.pop()
        else:
            print 'Unknown opcode {}'.format(opcode)


if __name__ == '__main__':
    """
    Unmarshall the code object from the .pyc file reference as a command
    line argument, and intrepret it.

    Usage: python interpreter.py 1.pyc
    """
    f = open(sys.argv[1], 'rb')
    code = parse_pyc(f)
    # dis.dis(code)  # helpful for debugging! but kinda cheating
    print('Interpreting {}...\n'.format(sys.argv[1]))
    ret = interpret(code)
    print('\nFinished interpreting, and returned {}'.format(ret))
