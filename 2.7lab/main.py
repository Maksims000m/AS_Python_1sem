def count_paragraphs(filename):
  with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

  paragraphs = [p for p in content.split('\n\n') if p.strip()]
   
  return len(paragraphs)

def main():
  filename = 'text.txt'
  num_paragraphs = count_paragraphs(filename)
   
  print(f"Количество абзацев в тексте: {num_paragraphs}")

if __name__ == "__main__":
  main()
