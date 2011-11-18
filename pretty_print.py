from random import randint

str = "etaelehoyrnrsweeneiornvtsdelreiolrertsrhotruongpmghwsihlxtdeelaneeetldosheeralithtndareluttelderrocltaeiwrtodeoeyladfswpsremeucraddfvrntaiansudynaeytnaidthioicheegblyoeielsvvneoliiudveieuaoaodptetpurrdeieecnohasapiwdoehltflsbohlamthioeosistssbstwe"
str2 = "cesaleomrnu"
str3 = "flokwnot"

def get_dict(fname):
  """Parses word list; sorts words in alpha order and stores in a dict for
     later access"""

  f = open( fname )
  words = f.readlines()
  w = dict()

  for word in words:
    k = ''.join(sorted(word.strip()))
    if not k: continue
    w[k] = word.strip()

  return w

def get_random_string(length = 3000):
  alphabet = "aeiouqwertyuiaeiouopasdfgaeiouhjklzxcvbnm"
  str = ""
  for idx in range(length):
    str = str + alphabet[randint(0, len(alphabet)-1)]
  return str


def main():
  #str = get_random_string()
  print str
  mydict = get_dict("words.txt")
  res = dict()

  for start in range(len(str)):
    # print "start=%d" %start
    for l in range(1,21):
      # print "length=%d" %l
      splice = str[start:start+l]
      #print "%d:%d:%s" %(start, l, splice)
      w = ''.join(sorted(splice))
      if w in mydict:
        #print "[%d]%s:%s[%d]" %(start, splice, mydict[w], start+len(splice)-1)
        res[start] = mydict[w]

  # for k in sorted(res.keys()):
  #   print "[%d]%s" %(k, res[k])

  idx = sorted(res.keys())[0]
  ans = '-' * idx
  #print "BEGIN:%d:%s" %(idx,ans)
  pad = 0
  while idx < len(str):
    if not (idx in res):
      idx = idx + 1
      ans = ans + '-'
      pad = pad + 1
      continue

    ans = ans + res[idx]
    idx = idx + len(res[idx])

  print ans
  print "padding: %d" %pad

if __name__ == '__main__':
  main()
