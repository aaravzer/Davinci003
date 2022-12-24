import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response['choices'][0]['text']

while True:

  prompt = input('Prompt: ')
  print('Generating...')
  completion = generate(prompt)
  x = input(f"Completion Result:\n\n{completion}\n\n1.) Continue\n2.) Regenerate\n\nOption: ")
  if x != '1':
    continue
  
  with open('dataset.json') as dataset:
    dataset_json = json.load(dataset)

  new_set = {
    'prompt': f"Write a unique and plagiarism-free essay about {prompt}",
    'completion': completion,
  }

  dataset_json.append(new_set)
  with open('dataset.json', 'w') as dataset:
    json.dump(dataset_json, dataset, indent=4)
    print('\nDataset Saved\n')

