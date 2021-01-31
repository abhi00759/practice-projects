#!/usr/bin/env python
# coding: utf-8

# In[67]:


class Laptop:
    discount_percent=10   #class variable
    def __init__(self,name,model_name,price):
        self.name=name
        self.model_name=model_name
        self.price=price
        
    def apply_discount(self):
        dis_price=(self.discount_percent/100)*self.price
        return self.price-dis_price
    


# In[69]:



L1=Laptop('inspiron_3000','Dell',30000)
L2=Laptop('Hp','mk2000',45000)
L2.discount_percent=50


# In[71]:


print(L1.__dict__)


# In[63]:


print(L1.apply_discount())


# In[64]:


print(L2.apply_discount())


# In[51]:


class Circle:
    pi=3.14       #class variable
    def __init__(self,radius):
        #instance variables
        self.radius=radius
    def  calc_circumference(self):
        return 2*self.radius*Circle.pi


# In[52]:


C1=Circle(5)
C2=Circle(10)


# In[54]:


print(C1.calc_circumference())


# In[39]:


print(C2.calc_circumference())


# In[25]:


class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age


# In[26]:


P1=Person('Abhishek','Ranjan',23)
P2=Person('Ayushi','Anand',22)
P3=Person('Anurag','kumar',22)


# In[27]:


print(Person.count_instance)


# In[ ]:




