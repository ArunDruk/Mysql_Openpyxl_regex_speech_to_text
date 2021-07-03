def list_squares():
    L=[43, 21, 76, 98]
    result=list(map(lambda i:i*i , L ))
    print(result,list_squares.__name__)


list_squares()