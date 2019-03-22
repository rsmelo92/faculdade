from lexer import Lexer
from parser import Parser
from codegen import CodeGen
import os

fname = "input.bonoro"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")

os.system("llc -filetype=obj output.ll")
os.system("clang output.o -o output")
os.system("./output")
