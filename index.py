import requests
from bs4 import BeautifulSoup
# from openxl import W

urls = ["https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-bar-chart-of-average-rainfall-by-month-from-ielts-high-scorers-choice-series-academic-set-1/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-pie-charts-of-electricity-generation-by-source-from-ielts-high-scorers-choice-series-academic-set-1/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-two-tables-comparing-workers-of-foreign-and-us-birth-in-the-united-states-from-ielts-high-scorers-choice-series-academic-set-1/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-bar-chart-and-pie-chart-describing-australian-water-consumption-from-ielts-high-scorers-choice-series-academic-set-1/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-process-diagram-describing-the-cycle-of-pollution-from-ielts-high-scorers-choice-series-academic-set-1/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-two-pie-charts-describing-uk-tax-revenue-and-government-spending-from-ielts-high-scorers-choice-series-academic-set-2/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-multiple-line-graph-describing-the-percentage-of-students-learning-a-second-language-from-ielts-high-scorers-choice-series-academic-set-2/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-table-and-pie-chart-describing-day-and-overnight-stays-in-public-and-private-hospitals-in-australia-from-ielts-high-scorers-choice-series-academic-set-2/"
]

essay_list=[]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    g_1 = soup.find_all("div", class_="g-1")[0]

    paragraphs = g_1.find_next_siblings("p")

    essay = []
    for paragraph in paragraphs:
        if not paragraph.find_all(recursive=False):
            essay.append(paragraph.text)
            
    essay_list.append(essay)

print(essay_list)


