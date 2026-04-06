
from src.logic import mask_random_letters
def test_masking_length():
  word="panda"
  display,hidden=mask_random_letters(word)
  assert len(display)==len(word)
  assert len(hidden)in [2,3]
  print("passed")
if __name__=="__main__"
test_masking_length()
