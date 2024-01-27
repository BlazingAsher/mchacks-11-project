import os


class CodeParser:


    output_path = "output.txt"

    
    def __init__(self, code_path):

        self.code_path = code_path
        

    def run_c_code(self):
        input_file = open(self.code_path, "r")
        c_file = open("main.c", "w")


        for line in input_file:
            c_file.write(line)

        input_file.close()
        c_file.close()

        os.system("gcc main.c")
        os.system("./a.out >> %s" % self.output_path)

        os.remove("main.c")
        os.remove("a.out")


    def print_code_output(self):
        output = ""
        output_file = open(self.output_path, "r")

        for line in output_file:
            output += line

        output_file.close()


        os.remove(self.output_path)

        return output




parser = CodeParser("code.txt")
parser.run_c_code()
print(parser.print_code_output())





