import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

urls = ["https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-process-diagram-describing-the-life-cycle-of-the-car-from-ielts-high-scorers-choice-series-academic-set-2/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-bar-chart-of-scotlands-exports-from-ielts-high-scorers-choice-series-academic-set-3/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-two-bar-charts-on-obesity-from-ielts-high-scorers-choice-series-academic-set-3/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-5-line-graphs-visitor-spend-from-ielts-high-scorers-choice-series-academic-set-3/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-multiple-bar-chart-us-export-markets-from-ielts-high-scorers-choice-series-academic-set-3/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-flow-charts-circles-poverty-from-ielts-high-scorers-choice-series-academic-set-3/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-pie-charts-greenhouse-gas-from-ielts-high-scorers-choice-series-academic-set-4/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-double-line-graph-hospital-stays-from-ielts-high-scorers-choice-series-academic-set-4/",
"https://www.ielts-blog.com/ielts-writing-samples/ielts-reports-band-9/ielts-report-topic-table-road-traffic-london-from-ielts-high-scorers-choice-series-academic-set-4/"
]



essay_list=[]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    g_1 = soup.find_all("div", class_="g-1")[0]

    paragraphs = g_1.find_next_siblings("p")

    # images = soup.find_all("noscript")[2].find_previous_siblings()
    
    # print(images[0]['data-lazy-src'])
    essay = []
    for paragraph in paragraphs:
        if not paragraph.find_all(recursive=False):
            essay.append(paragraph.text)
            # ws.append()
            # ws.append([str(essay), 9])
            # print('ESSXX', essay)
    essay_list.append(essay)


wb = load_workbook('./dataset.xlsx')
ws = wb.active

for i in essay_list:
    print(str(i))
    ws.append([str(i), "9"])
print(essay_list)


wb.save('./dataset.xlsx')


