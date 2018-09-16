# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:11:11 2018

@author: Sang
"""

import hgtk
import re

josa_list = ['들', '까지','도', '하는', '뿐만', '은', '는', '에서', '께', '에', '가', '의', '와', '와의', '에게서', '으로', '로부터', '에게', '랑', '치고', '라고', '하고', '을', '대로', '로서', '같이', '마저', '으로써', '보다', '만', '께서', '엔들', '까지', '인즉', '에서부터', '에다', '인들', '를', '들', '조차', '밖에', '한테', '과', '처럼', '이며', '이', '으로서', '로써', '으로부터', '부터', '뿐']

def get_count(word, ojoels):
    num = 0
    for ojoel in ojoels:
        if word in ojoel:
            num += 1
    return num

def check_if_word(word, ojoels, threshold=0.5): #threshold는 num_josa_ojoels/total_num_ojoels
    is_word = 0
    total_num_ojoels = 0 # 해당 단어가 들어가는 어절이 몇개가 있는지를 저장
    num_josa_ojoels = 0 # 해당 단어가 들어간 어절 중에서 단어 뒤의 부분이 조사인 어절의 수
    for ojoel in ojoels:
        if ojoel.find(word) > -1:
            total_num_ojoels += 1
            suffix = ojoel[len(word):]
            if suffix in josa_list:
                num_josa_ojoels += 1
    if num_josa_ojoels/total_num_ojoels > threshold:
        is_word = 1
    else:
        is_word = 0
    return is_word  

def check_if_not_Noun(word):
    Except_words =['것']
    Batchims = ['ㅆ', 'ㅀ', 'ㄾ', 'ㄶ','ㄵ']
    is_not_Noun = 0
    for batchim in Batchims:
        if batchim in hgtk.text.decompose(word):
            is_not_Noun = 1
            break
    if is_not_Noun == 0:
        for except_word in Except_words:
            if except_word in word:
                is_not_Noun = 1
                break
    if word != '곳간':
        if word[0] == '곳':
            is_not_Noun = 1
            
    return is_not_Noun

def get_repetitive(word, words_list):
    repetitives = []
    for org_word in words_list:
        if len(org_word) > len(word):
            if word in org_word:
                repetitives.append(org_word)
    return repetitives

def check_if_josa(repetitives):
    repetitive_words = []
    repetitives = sorted(repetitives, key=lambda x:len(x))
    shortest_word = repetitives[0]
    for word in repetitives[1:]:
        for josa in josa_list:
            if word[len(shortest_word):] in josa[0:len(word)-len(shortest_word)]:
                repetitive_words.append(word)
    return repetitive_words

def get_repetitives(words_list):
    repetitive_words = []
    for word in words_list:
        word_count = 0
        for word1 in words_list:
            if word in word1:
                word_count += 1
                if word_count > 1:
                    break
        if word_count > 1:
            repetitives = []
            repetitives.append(word)
            repetitives.extend(get_repetitive(word, words_list))
            repetitive_words.extend(check_if_josa(repetitives))
    return set(repetitive_words)
    
def extract(text, FREQ=0, THRESHOLD=0.5):
    text1 = re.sub(r'[\(\)\'\"=~…]', ' ', text)
    text1 = re.sub(r'\.','',text1)
    cleaned_text = re.sub(r'[^∙\s\w\d]', '', text1) # 기호 없애기
    cleaned_text = cleaned_text.replace('\n', ' ') # new line 없애기
    ojoels = cleaned_text.split() # 한국어의 어절 추출
    
    word_counts= {} # 단어라고 간주되는 것을 키로 저장하고, 그것의 출현 빈도를 value로 저장
    for ojoel in ojoels:
        if len(ojoel) < 2: # 어절의 음절수가 하나인 경우는 제외
            continue
        for k in range(2, len(ojoel)+1):
            word = ojoel[0:k]
            if word not in word_counts.keys():
                word_counts[word] = get_count(word, ojoels)    
                
    sorted_words = list(sorted(word_counts.items(), key=lambda x:x[1], reverse=True))
    
    Noun_words = []
    for word, fre in sorted_words:
        if fre > FREQ:  # 사용된 빈도수에 따라서 1차 제거
            if check_if_word(word, ojoels, THRESHOLD):
                Noun_words.append(word)
    
    final_Noun_words=[]
    for word in Noun_words:
        if not check_if_not_Noun(word):
            final_Noun_words.append(word)
         
    repetitive_words = list(get_repetitives(final_Noun_words))
    
    for word in repetitive_words:
        final_Noun_words.remove(word)
    
            
    return final_Noun_words
