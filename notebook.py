
# coding: utf-8

# In[22]:


teste = "Aula de analise de sentimentos e python basico"


# In[23]:


len(teste)

#teste de inversao
print(teste[::-1])

#retorna a posicao onde inicia uma palavra
print(teste.find('python'))

#multiplica string
print((teste + ' ')  *2)


# In[24]:


teste = teste.replace('basico', 'avancado')
print (teste)


# In[33]:


teste.count('a')


# In[34]:


teste.find('l')


# In[35]:


teste[2]


# In[36]:


teste.split()


# In[37]:


' some '.join(teste.split('a'))


# In[38]:


teste.upper()


# In[39]:


teste.lower()


# In[25]:


teste.lower().capitalize()


# In[26]:


teste.lower().title()


# In[27]:


teste.swapcase()


# In[28]:


'UPPER'.isupper()


# In[29]:


'UpperR'.isupper()


# In[30]:


'UpperR'.isupper()


# In[31]:


'lower'.islower()


# In[32]:


'Lower'.islower()


# In[40]:


'Isso E Um Titulo'.istitle()


# In[41]:


'Isso e um Titulo'.istitle()


# In[42]:


'aa44'.isalnum()


# In[43]:


'a$44'.isalnum()


# In[44]:


'letters'.isalpha()


# In[45]:


'letters4'.isalpha()


# In[46]:


'306090'.isdigit()


# In[47]:


'30-60-90 Triangle'.isdigit()


# In[48]:


'   '.isspace()


# In[49]:


''.isspace()


# In[50]:


'A string.'.ljust(15)


# In[51]:


'A string.'.rjust(15)


# In[52]:


'A string.'.center(15)


# In[53]:


'String.'.rjust(15).strip()


# In[54]:


'String.'.ljust(15).rstrip()


# In[55]:


import re


# In[56]:


test = 'This is for testing regular expressions in Python.'


# In[58]:


result = re.search('This', test)
print(result)


# In[59]:


result = re.search ('(Th)(is)',test)


# In[60]:


result.group(1)


# In[61]:


result.group(2)


# In[62]:


result.group(0)


# In[65]:


result = re.match ('regular', test)
print(result)


# In[67]:


result = re.match ('(....................)(regular)', test)
print (result)


# In[68]:


result.group(0)


# In[69]:


result.group(2)


# In[70]:


result = re.match('(.{20})(regular)', test)


# In[71]:


result.group(0)


# In[72]:


result.group(1)


# In[73]:


result.group(2)


# In[74]:


result = re.match ('(.{10,20})(regular)', test)


# In[75]:


result.group(0)


# In[76]:


result = re.match('(.{10,20})(testing)', test)


# In[78]:


result.group(0)


# In[79]:


anotherTest = 'a cat, a dog, a goat, a person'


# In[80]:


result = re.match('(.{5,20})(,)', anotherTest)


# In[81]:


result.group(1)


# In[82]:


result = re.match('(.{5,20}?)(,)', anotherTest)


# In[83]:


result.group(1)


# In[84]:


anotherTest = '012345'


# In[85]:


result = re.match('01?', anotherTest)


# In[86]:


result.group(0)


# In[87]:


result = re.match('0123456?', anotherTest)


# In[90]:


result.group(0)


# In[98]:


#substituindo strings com expressão regulares
print(anotherTest)
result = re.sub('01?', 'gab',anotherTest)
print(result)

