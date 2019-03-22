; ModuleID = "/home/rsmelo/Documents/github/python/bonoro/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = add i8 40, 40
  %".3" = mul i8 20, 2
  %".4" = udiv i8 %".3", 10
  %".5" = sub i8 %".2", %".4"
  %".6" = bitcast [5 x i8]* @"fstr" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8 %".5")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"