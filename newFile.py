import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

urls = ["https://www.ielts-blog.com/category/ielts-writing-samples/ielts-reports-band-7/","https://www.ielts-blog.com/category/ielts-writing-samples/ielts-reports-band-8/"]

url = "https://www.ielts-blog.com/category/ielts-writing-samples/ielts-reports-band-8/"

links = []

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
g_1 = soup.find_all("div", class_="g-1")[0]
paragraphs = g_1.find_next_siblings("p")
for paragraph in paragraphs:
   try:
        if paragraph:
                a_tag = paragraph.find('a')
                if a_tag:
                    links.append(a_tag['href'])
                else:
                    print("No <a> tag found.")
        else:
            print("No paragraph_tag found.")
   except Exception as e:
        print(f"Error: {e}")
    

print(links)
print(len(links))
    # g_1 = soup.find_all("div", class_="entry-content")[0]

# links = []
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# g_1 = soup.find_all("div", class_="entry-content")[0]

# for paragraph_tag in g_1:
#     try:
#         if paragraph_tag:
#             strong_tag = paragraph_tag.find('strong')
#             if strong_tag:
#                 a_tag = strong_tag.find('a')
#                 if a_tag:
#                     # print(a_tag['href'])
#                     links.append(a_tag['href'])
#                 else:
#                     print("No <a> tag found.")
#             else:
#                 print("No <strong> tag found.")
#         else:
#             print("No paragraph_tag found.")
#     except Exception as e:
#         print(f"Error: {e}")
        

# print(links)
# print(len(links))


essay_list=[]
imagesList = []
for url in links:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    g_1 = soup.find_all("div", class_="g-1")[0]

    paragraphs = g_1.find_next_siblings("p")

    images = soup.find_all("noscript")[2].find_previous_siblings()
    img_link = images[0]['data-lazy-src']
    print(img_link)
    imagesList.append(img_link)
    # print(images[0]['data-lazy-src'])
    extract_text = True
    essay = []
    for paragraph in paragraphs:
        if paragraph.find('em'):
            extract_text = False  # Set the flag to False when a paragraph with <em> tag is found
        if extract_text:
            # print(paragraph.text)
            essay.append(paragraph.text)
        # if not paragraph.find_all(recursive=False):
            # essay.append(paragraph.text)
            # ws.append()
            # ws.append([str(essay), 9])
            # print('ESSXX', essay)
    essay_list.append(essay)


wb = load_workbook('./datasetImages.xlsx')
ws = wb.active

for i in range(len(essay_list)):
    print(i)
    # print(str(i))
    ws.append([str(imagesList[i]), str(essay_list[i]), str("8")])
print(essay_list)


wb.save('./datasetImages.xlsx')



