Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #question 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7/3
2.3333333333333335
>>> 7//3
2
>>> 6==6
True
>>> a=20; a+=30; a%=3;
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7>4) or (18==3)) and (9>3)
True
>>> True is False
False
>>> False is 'False'
False
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> #question 3
>>> s1="nice to have it"
>>> s2="here"
>>> s3=s1 + s2
>>> 
>>> s3
'nice to have ithere'
>>> # question 4
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3]
[5, [100, 200, ['hello']], 23, 11]
>>> a[3][1][2]
['hello']
>>> #question 5
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a.insert(0,"nice to have it")
>>> a.insert(7,"here")
>>> a
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #question 6
>>> h = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
SyntaxError: invalid syntax
>>> #question 7
>>> colour_list_1=set(["white", "black","red"])
>>> colour_list_2=set(["red", "green"])
>>> colour_list_1.difference(colour_list_2)
{'black', 'white'}
>>> 