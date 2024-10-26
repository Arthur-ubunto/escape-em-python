fomatter = " {} {} {} {}"
#peguei a variavel, e coloquei os valores em ordem, com format
print(fomatter.format(1,2,3,4))
print(fomatter.format("one","two","tree","four"))
print(fomatter.format(True,False,True,False))
print(fomatter.format(fomatter,fomatter,fomatter,fomatter))
print(fomatter.format(
    "try your",
    "owm text here",
    "maybe a poem",
    "or a song about fear"
))