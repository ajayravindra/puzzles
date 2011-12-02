##
# reverse_words_in_sentence.py
#   strides (::) work some wonders to make this simple solution possible
##

def reverse_sentence( sentence ):
  return ' '.join([ word[::-1] for word in sentence.split()])[::-1]

if __name__ == '__main__':
  sentence = raw_input( "enter sentence: ")
  print sentence
  print reverse_sentence( sentence )

