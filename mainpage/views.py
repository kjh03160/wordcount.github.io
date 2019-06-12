from django.shortcuts import render
import re
# Create your views here.

# context  > dic 형 데이터를 home.html에 보내준다

def index(request):
    a = 10
    context = {
        'number' : a,
    }
    return render(request, 'index.html', context)

def count(request):

    fulltext = request.GET['fulltext'] # form tag 안의 textarea name을 써줌
    
    text = fulltext.split() # 띄어쓰기로 나눠주기

    sentence = fulltext.split()
    sentence = ''.join(sentence)
    sentence = re.split(r"[\:\.\!\?]", sentence)

    dict = {}


    for elem in text:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1
    dict_sort = sorted(dict.items(), reverse=True, key = lambda x:x[1])
    # item_list = list(dict.items())

    # word_list = list(dict.keys())

    # value_list = list(dict.values())
    # index_list = []

    # for i in value_list:
    #     index_list.append(value_list.index(i))


    # sort_dict = {}
    # for i in range(len(value_list)):
    #     sort_dict[value_list[i]] = index_list[i]


    # sort_items = sorted(sort_dict.items(), reverse=True)
    # sort_index = []
    # for i in sort_items:
    #     sort_index.append(i[1])

    # sort_word = []
    # for i in sort_index:
    #     sort_word.append(word_list[i])

    # sort_frequency = sorted(sort_dict.keys(), reverse=True)

    # result_dict = {}
    # for i in range(len(sort_word)):
    #     result_dict[sort_word[i]] = sort_frequency[i]


    current = 0
    for spell in text:
        temp = current
        first = len(spell)
        current = first + temp
    length = current
    
    


    sentence_length = len(sentence) - 1
    word = list(dict.keys())
    word_frequency = list(dict.values())
    word_length = len(word_frequency)
    density_list = {}
    # density 구하기....
    for word in word:
        for frequency in word_frequency:
            denstiy = round((frequency / word_length), -2) * 100
            density_list[word] = denstiy
    


    context = {
        'fulltext' : fulltext,
        'dict' : dict_sort,
        'length' : length,
        'sentence_length' : sentence_length,
        'word_length' : word_length,
        'density_list' : density_list.items(),

    }
    return render(request, 'count.html', context)


