#! usr/bin/env  python
def demo(num,*args,**kwargs):

    print(num)
    print(args)
    print(kwargs)

demo(1,2,3,4,5,6,name="小明",age=18,gender=True)
