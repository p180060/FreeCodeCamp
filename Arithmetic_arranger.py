#!/usr/bin/env python
# coding: utf-8

# In[389]:


def arithmetic_arranger(problems,solve="False"):
    if(len(problems) > 5):
        return "Error: Too many problems."
    firstnumber=""
    operatornumber=""
    secondnumber=""
    linenumber=""
    sumnumber=""
    string=""
    for i in problems:
        first=i.split(" ")[0]
        operator=i.split(" ")[1]
        second=i.split(" ")[2]
        if (re.search("[a-z,A-Z]",i)):
            return "Error: Numbers must only contain digits."
        elif(re.search("[/]",i) or re.search("[*]",i)):
            return "Error: Operator must be '+' or '-'."
        elif(len(first) >= 5 or len(second) >= 5):
            return "Error: Numbers cannot be more than four digits."
        sum=""
        if(operator == "+"):
            sum=str(int(first) + int(second))
        elif(operator == "-"):
            sum=str(int(first) - int(second))
        length=max(len(first),len(second))+2
        top=str(first).rjust(length)
        bottom=operator+str(second).rjust(length-1)
        res=str(sum).rjust(length)
        line=""
        for j in range(length):
            line += "-"
        if(i != problems[-1]):
            firstnumber  +=  top +  '    '
            secondnumber +=  bottom + '    '
            linenumber += line + '    '
            sumnumber += res + '    '
        else:
            firstnumber  +=  top
            secondnumber +=  bottom
            linenumber += line
            sumnumber += res 
            
    if(solve == True):
        string = firstnumber + "\n" + secondnumber + "\n" + linenumber + "\n" +sumnumber
    else:
        string = str(firstnumber + "\n" + secondnumber + "\n" + linenumber)
    return(string)


# In[390]:


class UnitTests():
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        print(actual==expected)
        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        print(actual==expected)

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        print(actual==expected)
    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        print(actual==expected)
    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        print(actual==expected)
    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        if(actual==expected):
            print(True)
        else:
            print(False)


# In[391]:


T=UnitTests()
print(1)
T.test_arrangement()
print(2)
T.test_too_many_problems()
print(3)
T.test_incorrect_operator()
print(4)
T.test_too_many_digits()
print(5)
T.test_only_digits()
print(6)
T.test_solutions()


# In[ ]:




