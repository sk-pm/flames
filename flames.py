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

count=len(a)+len(b)
flames=["F","L","A","M","E","S"]
while len(flames) > 1:
    split_index = (count % len(flames) - 1)
    if split_index >= 0:
        right = flames[split_index + 1:]
        left = flames[:split_index]
        flames = right + left
    else:
        flames = flames[:len(flames) - 1]
if (st.button("FLAMES")):
    st.success("You are Relation is: {}".format(flames))
