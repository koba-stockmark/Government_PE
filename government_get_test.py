import json
import re
from government_news_analysis import GovernmentNewsAnalysis

model = GovernmentNewsAnalysis() # KeywordExtractorのクラスのインスタンス化

articles = json.load(open('../PredicateStructuring/data/nikkei.json'))
articles2 = json.load(open('../PredicateStructuring/data/nikkei_5000.json'))
solution2 = open('data/government_news.txt')
solution = open('data/government_add.txt')
solution3 = open('data/error_text.txt')

out_file2 = open('data/government_result.tsv', 'w')
#out_file = open('data/government_add.tsv', 'w')

#"""
for doc in solution2:
  for sep_doc in doc.splitlines():
#    keyword_list = model.government_action_extract(sep_doc) # 政府HP
    keyword_list = model.government_phase_extract(sep_doc) # ニュース記事
    ret = sep_doc + '\t' + keyword_list + '\n'
    print(ret)
    out_file2.write(ret)
out_file2.close()
"""
for doc in articles:
  for sep_doc in doc.splitlines():
    keyword_list = model.government_action_extract(sep_doc) # キーワードの候補の抽出
    ret = sep_doc + '\t' + keyword_list + '\n'
    print(ret)
    out_file2.write(ret)
out_file2.close()
"""