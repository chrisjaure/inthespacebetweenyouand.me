#!/usr/bin/env python3
import sys
import yaml
from string import Template

document = sys.argv[1]

if not document:
  print("Please provide a conversation!")
  sys.exit()

with open(document) as f:
  data = yaml.load(f, Loader=yaml.SafeLoader)

with open("template.html") as f:
  template = f.read().encode('utf-8').decode('utf-8')

s = Template(template)
conversation = ''

if 'messages' in data:
  for message in data['messages']:
    conversation = conversation + '<div class="{}">'.format(list(message.keys())[0])
    nested = list(message.values())[0]
    if not isinstance(nested, list):
      nested = [nested]
    for m in nested:
      conversation = conversation + '<div class="message">' + m + '</div>'
    conversation = conversation + '</div>'

print(
  s.substitute(title=data['title'],
  input=data['input'],
  conversation=conversation
).encode('utf-8').decode('utf-8'))

