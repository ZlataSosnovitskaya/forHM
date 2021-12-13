def find_all_rabin_karp(text, pattern): #  Алгоритм Рабина-Карпа для поиска вхождений образца в текст
    result = []
    patternsum = sum(ord(s) for s in pattern)
    textwindowsum = sum(ord(text[j]) for j in range(len(pattern)))
    text = text + ' '
    for i in range(len(text) - len(pattern)):     
        if patternsum == textwindowsum:
            if text.startswith(pattern, i):
                result.append(i)
        textwindowsum = textwindowsum - ord(text[i])+ord(text[i+len(pattern)])      
    return result 
      