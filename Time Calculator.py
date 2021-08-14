#!/usr/bin/env python
# coding: utf-8

# In[284]:


def add_time(start,duration,day=False):
    day_in_week=["Monday","tuesday","Wednesday","Thursday","Friday","saturDay","Sunday"]
    index=0
    firststart=start.split(":")[0]
    last=start.split(":")[1]
    firstend=last.split(" ")[0]
    secondstart=duration.split(":")[0]
    last2=duration.split(":")[1]
    secondend=last2.split(" ")[0]
    ampm=last.split(" ")[1]
    hours=(int(firststart)+int(secondstart))
    minutes=(int(firstend)+int(secondend))
    amount_of_day=int(int(secondstart)//24)
    for i in range(len(day_in_week)):
        if(day == day_in_week[i]):
            index=i
    if(ampm == "PM" and (int(firststart)+int(secondstart)) >= 12):
        amount_of_day += 1
    x=amount_of_day+index
    print(x)
    x=x%7
    print(x)
    days=day_in_week[x]
    amount_of_ampm=int(firststart+secondstart)//12
    ampm_flip={"AM":"PM","PM":"AM"}
    ampm=ampm_flip[ampm] if amount_of_ampm % 2 == 1 else ampm
    if((minutes) >= 60):
        if (minutes) >= 60:
            (hours) += 1
            minutes = minutes % 60
    if(int(hours) > 12):
        hours  = int(hours)%12
    if(minutes < 9):
        minutes= "0"+str(minutes)
    if(hours == 0):
        hours=12
   
    if(amount_of_day >= 2):
        if(day):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)+", "+ days  +" (" +str(amount_of_day)+" days later)"
        if(day==False):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)+ " (" +str(amount_of_day)+" days later)"
    elif(amount_of_day == 1):
        if(day):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)+", "+ days  +" (next day)"
        if(day==False):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)+" (next day)"
    else:
        if(day):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)+", "+ days
        if(day==False):
            total=str(hours)+":"+str(minutes)+" "+str(ampm)
    print(total)
    return(total)


# In[285]:


actual = add_time("8:16 PM", "466:02", "tuesday")
expected = "6:18 AM, Monday (20 days later)"
print(actual==expected)


# In[286]:


class UnitTests():

    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        print(actual==expected)
    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        print(actual==expected)

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        print(actual==expected)

    def test_period_change_at_twelve(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        print(actual==expected)

    def test_twenty_four(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        print(actual==expected)

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        print(actual==expected)

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        print(actual==expected)

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        print(actual==expected)

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        print(actual==expected)

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        print(actual==expected)

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        print(actual==expected)

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        print(actual==expected)


# In[287]:


t=UnitTests()
t.test_same_period()
t.test_different_period()
t.test_next_day()
t.test_period_change_at_twelve()
t.test_twenty_four()
t.test_two_days_later()
t.test_high_duration()
t.test_no_change()
t.test_same_period_with_day()
t.test_twenty_four_with_day()
t.test_two_days_later_with_day()
t.test_high_duration_with_day()


# In[ ]:





# In[ ]:




