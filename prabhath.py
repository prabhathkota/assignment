#!/bin/env python
#/*********************************************/
# * Date        :   15th Jan 2019
# * Description :   This python module parses INPUT file and gives output text file
# * Author      :   Prabhath Kota
# * How to use  :   type input.txt | prabhath.py > output.txt (Windows)
#               :   cat input.txt | prabhath.py > output.txt (Linux)
#/*********************************************/
import sys

star_dict = {}
dot_prev_line = ''
dot_prev_count = 0

def count_stars(each_line):
  star_count = 0
  star_count = each_line.count('*')
  return star_count

def count_dots(each_line):
  dot_count = 0
  dot_count = each_line.count('.')
  return dot_count

def reset_star_dict(start_count):
  for each in star_dict.keys():
    if each > start_count:
      del star_dict[each]

def reset_prev_dot_data():
  global dot_prev_count
  global dot_prev_line  
  dot_prev_line = ''
  dot_prev_count = 0

def get_dot_val(each_line):
  dot_str = ''
  dot_count = count_dots(each_line)
  dot_str += '\t' * (dot_count)
  global dot_prev_count
  global dot_prev_line
  if not dot_prev_count:
    pass
    dot_prev_count = dot_count
    dot_prev_line = ''
    dot_str += '-'
  else:
    if dot_count > dot_prev_count:
      dot_str += '+'
    else:
      dot_str += '-'
  return dot_str

def get_star_val(each_line):
  start_val = ''
  start_count = count_stars(each_line)
  if start_count == 1:
    if start_count not in star_dict:
      star_dict[start_count] = 1
      start_val = 1
    else:
      star_dict[start_count] = star_dict[start_count] + 1
      start_val = star_dict[start_count] 
  else:
    reset_star_dict(start_count)
    if start_count not in star_dict:
      star_dict[start_count] = 1
    else:
      star_dict[start_count] = star_dict[start_count] + 1
    for each in star_dict:
      start_val = str(start_val) + str(star_dict[each]) + '.'
    start_val = start_val.rstrip('.')
  return start_val

arr = []
prev_dot_val = ''
for each in sys.stdin:
  if len(each) == 0:
    continue
  each_line = each.strip()
  if each_line.startswith('*'):
    reset_prev_dot_data()
    start_val = get_star_val(each_line)
    arr.append(str(start_val) + each_line.replace('*', ''))
  elif each_line.startswith('.'):
    dot_val = get_dot_val(each_line)
    dot_count = count_dots(each_line)
    prev_dot_val = dot_count
    arr.append(str(dot_val) + each_line.replace('.', ''))
  else:
    if prev_dot_val:
      arr.append('\t'*prev_dot_val + '  ' + each_line)

for x, y in zip(arr, arr[1:]):
  count_tabs_in_x = x.count('\t') 
  count_tabs_in_y = y.count('\t')
  #if count_tabs_in_x:
  if count_tabs_in_y > count_tabs_in_x:
      x = x.replace('-', '+')
  else:
      x = x.replace('+', '-')
  print x
print arr[-1]


