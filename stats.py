def count_words(g):
  words = g.split()
  return len(words) 

def number_of_characters(g):
    c = g.lower()
    dic = {}
    for ch in c:
        if ch.isalpha():          
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
    return dic



def convert(a):
  list1=[]
  for key,value in a.items():
    list1.append((key,value))

  result= []
  for key,value in list1:
    result.append({"name": key, "num":value})
  return result 


def sort_on(items):
  return items["num"]

def print_sorted(k):
  for item in k:
    if item["name"].isalpha():
      print(f'{item["name"]}: {item["num"]}')


#def sort(k):
 # k.sort(reverse=True, key=sort_on)
 # return(k)

