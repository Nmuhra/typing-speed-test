import time
string="exploit inside position"
wordcount=len(string.split())
print(string)
while True:
  t0=time.time()
  txt= str(input("Type the sentence:"))
  t1=time.time()
  accuracy=len(set(txt.split())&set(string.split()))
  accuracy=accuracy/wordcount
  time=t1-t0
  wpm=round(wordcount/time)
  print("WPM",wpm,\n"Accuracy",accuracy,\n"Time",time)
