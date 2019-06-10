from django.shortcuts import render

# Create your views here.

# context  > dic 형 데이터를 home.html에 보내준다

def home(request):
    a = 10
    context = {
        'number' : a,
    }
    return render(request, 'index.html', context)

def count(request):

    fulltext = request.GET['fulltext'] # form tag 안의 textarea name을 써줌
    
    text = fulltext.split() # 띄어쓰기로 나눠주기
    
    sentence = fulltext.split(".")

    dict = {}


    for elem in text:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

    current = 0
    for spell in text:
        temp = current
        first = len(spell)
        current = first + temp
    length = current
    
    


    sentence_length = len(sentence)
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
        'dict' : dict.items(),
        'length' : length,
        'sentence_length' : sentence_length,
        'word_length' : word_length,
        'density_list' : density_list.items(),

    }
    return render(request, 'count.html', context)


