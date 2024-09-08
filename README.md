*Note: Python is not my first language (C# is) so the code may be a little rusty...
# TabulateExample
A python script to ease importing a CSV file into tabluate (`> pip install tabulate`).

Tabulate requires data in the format of

`[['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3']]`,

but Python opens a CSV file as

`['A1,B1,C1\n','A2,B2,C2\n','A3,B3,C3'\n]`.

===NOTE: `\n` is how windows tells the computer that the next bit of data should be written on the next line.===

This confuses tabulate, and when you try to `tablate.tabulate(table)`, this happens:
```
-  -  -  -  -  -  -  -  -  -
A  1  ,  B  1  ,  C  1  \  n
A  2  ,  B  2  ,  C  2  \  n
A  3  ,  B  3  ,  C  3  \  n
-  -  -  -  -  -  -  -  -  -
```
...which is quite the mess (don't even get me started on using this with headers!).

This python script therefore fixes the tabulate CSV issue, and gives the desired output:
```
--  --  --
A1  B1  C1
A2  B2  C2
A3  B3  C3
--  --  --
```
This script though comes preloaded with a sample RabbitBytes.csv file, and splits it into the following headers - Name, YoB, Age, Carrots:
```
Name        YoB    Age    Carrots
--------  -----  -----  ---------
Alice      2005     19          3
Bob        2007     17          2
Caroline   2004     20          5
Dean       2006     18          1
Eve        2008     16          4
```
This script was made specifically for S.M.
