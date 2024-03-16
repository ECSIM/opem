# -*- coding: utf-8 -*-
'''
>>> import os
>>> import shutil
>>> from opem.Functions import *
>>> data=[i for i in range(100)]
>>> integrate(data,1)
4867.666666666666
>>> data[0]=None
>>> integrate(data,1)
>>> linear_plot([1,2,3],[2,4,6])
[[2.0, 4.0, 6.0], 0.0, 2.0]
>>> linear_plot([1,2,3],[2,4,None])
[[2.0, 4.0, None], 0.0, 2.0]
>>> estimate_coef([0,0,0], [0,0,0])
[0, 0]
>>> get_precision(2)
0
>>> get_precision(2.55)
2
>>> warning_check_1(-0.2, 10, 20, True)
[True, 10]
>>> warning_check_1(-0.2, 10, 20, False)
[True, 20]
>>> rounder(22.2223, digit=2)
22.22
>>> rounder(22, digit=2)
22
>>> rounder("test")
'test'
>>> isfloat("2")
True
>>> isfloat("2.02")
True
>>> isfloat('ss')
False
>>> filter_lambda({"lambda":24})
[Warning] Opem Automatically Set Lambda To Maximum Value (23)
{'lambda': 23}
>>> filter_alpha({"alpha":2})
[Warning] Opem Automatically Set Alpha To Maximum Value (1)
{'alpha': 1}
>>> filter_lambda({"lambda":13})
[Warning] Opem Automatically Set Lambda To Minimum Value (14)
{'lambda': 23}
>>> filter_alpha({"alpha":-0.1})
[Warning] Opem Automatically Set Alpha To Maximum Value (0)
{'alpha': 0}
>>> filter_range(0,100,0.1)
[0, 100, 0.1]
>>> filter_range(500,0,0.1)
[0, 500, 0.1]
>>> filter_range(500,0,-0.1)
[0, 500, 0.1]
>>> Input_dict=Get_Input({"T": "Cell Operation Temperature [K]", "PH2": "Partial Pressure [atm]", "PO2": "Partial Pressure [atm]"},input_item=input_test)
>>> Input_keys=list(Input_dict)
>>> Input_keys.sort()
>>> print(Input_keys)
['Name', 'PH2', 'PO2', 'T']
>>> description_print("Model1",{"Model1":"Test"})
###########
Model1 :
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Test
<BLANKLINE>
<BLANKLINE>
###########
>>> check_update(1.4)
>>> check_update(0.1)
###########
...
Website : http://www.ecsim.site/opem
###########
>>> file1 = CSV_Init(OutputParamsKeys=["1","2","3"], OutputParams={"1":"1", "2":"2", "3":"3"}, Title="CSV_Test", Name="CSV_Test", Folder=os.path.join("CSV_Folder1", "CSV_Folder2"))
>>> file2 = CSV_Init(OutputParamsKeys=["1","2","3"], OutputParams={"1":"1", "2":"2", "3":"3"}, Title="CSV_Test", Name="CSV_Test2", Folder=os.path.join("CSV_Folder1", "CSV_Folder2"))
>>> file1.close()
>>> file2.close()
>>> sorted(os.listdir(os.path.join("CSV_Folder1", "CSV_Folder2", "CSV_Test"))) == ["CSV_Test.csv", "CSV_Test2.csv"]
True
>>> file1 = HTML_Init(Title="HTML_Test", Name="HTML_Test", Folder=os.path.join("HTML_Folder1", "HTML_Folder2"))
>>> file2 = HTML_Init(Title="HTML_Test", Name="HTML_Test2", Folder=os.path.join("HTML_Folder1", "HTML_Folder2"))
>>> file1.close()
>>> file2.close()
>>> sorted(os.listdir(os.path.join("HTML_Folder1", "HTML_Folder2", "HTML_Test"))) == ["HTML_Test.html", "HTML_Test2.html"]
True
>>> file1 = Output_Init(InputDict={"1":"1"}, Title="OPEM_Test", Name="OPEM_Test", Folder=os.path.join("OPEM_Folder1", "OPEM_Folder2"))
>>> file2 = Output_Init(InputDict={"1":"1"}, Title="OPEM_Test", Name="OPEM_Test2", Folder=os.path.join("OPEM_Folder1", "OPEM_Folder2"))
>>> file1.close()
>>> file2.close()
>>> sorted(os.listdir(os.path.join("OPEM_Folder1", "OPEM_Folder2", "OPEM_Test"))) == ["OPEM_Test.opem", "OPEM_Test2.opem"]
True
>>> shutil.rmtree("CSV_Folder1")
>>> shutil.rmtree("HTML_Folder1")
>>> shutil.rmtree("OPEM_Folder1")

'''
