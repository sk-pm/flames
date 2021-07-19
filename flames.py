'''
NAME:FLAMES FUN GAME
Author:Shaik Peeramohidin
GitHub:https://github.com/sk-pm
'''
import streamlit as st
a=st.text_input("Enter Your Name:")
b=st.text_input("Enter Your Crush Name:")
a=a.lower().replace(" ","")
b=b.lower().replace(" ","")
a=list(a)
b=list(b)
len_a=len(a)
len_b=len(b)
length=len_a+len_b
proceed = True

def rem_dup(a, b):
    for i in a:
        for j in b:
            if i == j:
                a.remove(j)
                b.remove(j)
                c = a + ['*'] + b
                return [c, True]
    c = a + ['*'] + b
    return [c, False]


while proceed:
    return_lst = rem_dup(a, b)
    con_list = return_lst[0]
    proceed = return_lst[1]
    str_index = con_list.index('*')
    a = con_list[:str_index]
    b = con_list[str_index + 1:]
try:
    if (st.button("FLAMES") and length!=0 ):
        count=len(a)+len(b)
        flames=["FRIENDSHIP","LOVE","AFFECTION","MARRIAGE","ENEMIES","SIBLINGS"]
        while len(flames) > 1:
            split_index = (count % len(flames) - 1)
            if split_index >= 0:
                right = flames[split_index + 1:]
                left = flames[:split_index]
                flames = right + left
            else:
                flames = flames[:len(flames) - 1]
        st.success("You are Relation is: {}".format(flames))
    else:
        st.text("Above fields can not be blank")
except:
    st.text("Above fields can not be blank")
