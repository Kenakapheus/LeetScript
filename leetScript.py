import re, time, sys

def execute(input, stack = [], direct_output = True, debug = False):
    commands = [r"(\d+),?\d*|\[[^]^[]*\]","##?","§","{","}",r"\(",r"\)","%","!","~","@",r"\<",r"\>",r"\.\.?"]   # list of viable commands
    matcher = re.compile("|".join("(?P<%s>%s)" % (chr(65+pointer), commands[i]) for i in range(0,len(commands)))).search  # building command regex
    times   = 0     # number of iterations
    output  = ""    # output string
    pointer = 0     # program pointer
    loop_stack = [] # stack for loops
    match = matcher(input)  # the match object of the current command
    while match is not None:    # continue as long as there are commands
        command = match.lastgroup   # the current command
        value   = match.group()     # the current value
        pointer = match.end()       # updating program pointer
        if command == 'A':      # add value to stack
            try:
                stack += [float(value.replace(',', '.'))] # is the value a number?
            except ValueError:
                stack += [value.strip('[]')]    #else add as string
        elif command == 'B':    # add or subtract the two last values of the stack
            v2 = stack.pop()
            v1 = stack.pop()
            if len(value) == 1: # add
                try:
                    stack += [v1 + v2]  # numbers are added
                except TypeError:
                    stack += [str(v1) + str(v2)] # string concatenated
            else:
                stack += [v1 - v2]  # subtract
        elif command == 'C':    # output the last value of the stack
            v1 = str(stack.pop())
            if direct_output:
                sys.stdout.write(v1)
            output += v1
        elif command == 'D':    # duplicate last value of the stack
            stack += [stack[-1]]
        elif command == 'E':    # remove last value from stack
            del stack[-1]
        elif command == 'F':    # start a loop
            loop_stack += [pointer]
        elif command == 'G':    # end a loop
            if loop_stack:
                v1 = loop_stack.pop()
                if stack and stack[-1]: # only loop if the last value of the stack is not zero
                    pointer = v1 - 1
        elif command == 'H':    # swap the last two values
            v1 = stack.pop()
            v2 = stack.pop()
            stack += [v1] + [v2]
        elif command == 'I':    # add a newline to the stack
            stack += ["\n"]
        elif command == 'J':    # do a regex sub
            stack += [re.sub(str(stack.pop()), str(stack.pop()), str(stack.pop()))]
        elif command == 'K':    # wait
            time.sleep(stack.pop())
        elif command == 'L':    # convert a string to its ordinal values
            for v1 in str(stack.pop()):
                stack += [ord(v1)]
        elif command == 'M':    # convert a ordinal value to a char
            stack += chr(int(stack.pop()))
        elif command == 'N':    # multiplication and division
            v2 = stack.pop()
            v1 = stack.pop()
            if len(value) == 1:
                stack += [v1 * v2]  # multiplication
            else:
                stack += [v1 / v2]  # division
        if debug:   # if debugging print the stack every iteration
            print(stack)
        times += 1  # count the iterations
        match = matcher(input, pointer) # fetch the next command
    return output, stack, times # return then output string, the stack and the number of iterations
    
#script = "5(!§{({!#§1##)}1##)"

#script = r"[World test][Hello \1\n][(?P<A>\w+)]~§"

#script = "100({100%##[% \U63;omplete!]#!#§1##0.25@)[Done!]§"

script = "0[Tokn`chmfoqhu`sdehkdrsnFnnfkd9]<1#>%(1#>%#%)}§!§9({10%##10.0[$bnlokdsd ]<1#>%(1#>%#%)}#!#§1##0,25@)0[Cnmd ]<1#>%(1#>%#%)}§"

#script = "0[Cnmd ]<1##>%(1##>%#%)}§"

output, s, times = execute(script)

#print(times)