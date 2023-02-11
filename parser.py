import sys
from classes import *

def parse_variable(line, set_variables):
    varname = line[16:].strip()
    set_variables[varname] = Set_Variables(varname, None)

def parse_construtor(line, constructors):
    const_name = line[16:line.find(",")]
    line = line[line.find(",")+2:]
    arity =int(line[6:7])
    temp_cv=line[33:].split()
    contravarients = [int(pos) for pos in temp_cv]
    constructors[const_name] = Constructor(const_name,arity,contravarients )

def parse_call(line, constructors):
    const_name = line[5: line.find(",")]
    args = [arg.strip() for arg in line[line.find(",") + 1:line.find(")")].split(", ")]
    return Call(constructors[const_name], args)

def parse_projection(line, constructors, set_variables):
    const_name = line[5:line.find(",")]
    line = line[line.find(",")+2:]
    set_name = line[:line.find(",")]
    index = int(line[line.find(",")+2])
    return Projection(constructors[const_name], set_variables[set_name], index)

def parse_expression(line, expressions, constructors, set_variables):
    line_split = [side.strip() for side in line.split("<=")]
    result = []
    for side in line_split:
        if side.startswith("call"):
            result.append(parse_call(side, constructors))
        elif side.startswith("proj"):
            result.append(parse_projection(side, constructors, set_variables))
        else:
            variable_name = side.strip()
            result.append(set_variables[variable_name])

    expressions.append(Expression(result[0], result[1]))



def parse_file(file_name):
    constructors = {}
    set_variables = {}
    expressions = []
    with open(file_name, "r") as f:

        lines = f.readlines()
        for line in lines:
            if line.startswith("def constructor"):
                parse_construtor(line, constructors)
            elif line.startswith("def set variable"):
                parse_variable(line, set_variables)
            else:
                parse_expression(line, expressions, constructors, set_variables )

    print(constructors)
    print(set_variables)
    print(expressions)

if __name__ == "__main__":
    filename = ""
    if len(sys.argv) == 1:
        filename = "example.txt"
    else:
        filename= sys.argv[1]

    print(parse_file(filename))
