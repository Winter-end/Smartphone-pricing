from bs4 import BeautifulSoup
import pandas as pd

with open('file.html', 'r', encoding='utf8') as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, 'html.parser')

processor = []
for i in soup.find_all('a'):
    if i.get('style') == "font-weight:500;":
        processor.append(i.string)

score = []
for i in soup.find_all('td'):
    try:
        classAttribute = i.div.get('class')
        if classAttribute == ['table-list-score-box']:
            score.append(i.div.string)
    except (IOError, AttributeError):
        pass

print(processor, score)

df = pd.DataFrame(
    {'processor' : processor,
     'score' : score}
)

df.to_csv('extra_data.csv', index = False)