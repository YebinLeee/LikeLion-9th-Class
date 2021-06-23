from django.shortcuts import render

# textarea box가 있는 home.html화면 렌더링 반환
def home(request):
    return render(request, 'home.html')

# textarea로부터 받은 문장
def result(request):
    sentence=request.GET['sentence']

    wordList=sentence.split()

    wordDict={}

    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1
    # 'result.html' 로부터 전체 문장, 그리고 딕셔너리로 만들어진 단어/단어개수 반환
    return render(request, 'result.html', {'fulltext':sentence, 'count':len(wordList), "wordDict":wordDict.items()})