from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from collections import Counter, defaultdict
from blog.models import essayData
import string
import operator

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def index(request):
    return render(request, 'blog/index.html')

# def submit(request):
#     return render(request, 'blog/results.html')

def results(request):
    if request.method == 'POST':
        # cast request essay as string and store
        text = str(request.POST.get('text'))
        # strip punctuation
        words_without_punc = text.translate(string.maketrans("",""), string.punctuation)
        # generate iterable of words
        words = words_without_punc.split()
        # count words
        word_list = Counter(words)

        essay_data = essayData(text=text, word_list = word_list)
        return render(request, 'blog/results.html', { 'search_results': essay_data})
    return render(request, 'blog/index.html')




def splitText(text):
    return text.split()

def removePunc(text):
    #syntax translate(find text (mapper), text to replace)
    return text.translate(string.maketrans("",""), string.punctuation)

def countWords(list):
    return Counter(list)

def taketextandcount(text):
    return splitText(removePunc(text))



#     #Collect All the words into a list
# for line in response:
#     #print "Line = " , line
#     line_words = line.split()
#     for word in line_words:  # looping each line and extracting words
#         each_word.append(word)

# #for every word collected, in dict same_words
# #if a key exists, such that key == word then increment Mapping Value by 1
# # Else add word as new key with mapped value as 1
# for words in each_word:
#     if words.lower() not in same_words.keys() :
#         same_words[words.lower()]=1
#     else:
#         same_words[words.lower()]=same_words[words.lower()]+1

# for each in same_words.keys():
#     print "word = ",each, ", count = ",same_words[each]