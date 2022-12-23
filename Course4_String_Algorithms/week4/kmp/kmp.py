# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  full_text = pattern + "$" + text
  count_array = [0]
  border = 0
  for ii in range(1, len(full_text)):
    while border > 0 and full_text[ii] != full_text[border]:
      border = count_array[border - 1]
    if full_text[ii] == full_text[border]:
      border = border + 1
    else:
      border = 0
    count_array.append(border)
  # Implement this function yourself
  for ii in range(len(pattern)+1, len(full_text)):
    if count_array[ii] == len(pattern):
      result.append(ii-2*len(pattern))
  return result

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

