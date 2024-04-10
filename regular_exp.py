import re


t = """
Long texts (longreads), 195.210.141.13 where big size combines with in-depth reporting, are becoming increasingly popular in print and online media, because these texts enable the publication to stand out against the information noise. The aim 195.210.142.13 s of this research are to identify the popularity of longreads in the Russian media and their content and compositional particularities. The research includes the monitoring of Russian federal publications and subsequent content analysi 195.210.144.11 s of 10 articles issued in 10 print and online publications. The key findings of the research indicate that longreads can be found in publications of different types from daily newspapers to niche news sites. As a rule, the texts are devoted to a description of a new phenomenon, their normal size being 2−4 thousand words. The usual longread composition scheme is an alternation of examples and generalizations.
"""


ip_candidates = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", 'cat')



print(ip_candidates)
