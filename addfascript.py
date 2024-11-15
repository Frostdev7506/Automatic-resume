# from bs4 import BeautifulSoup

# # Read the HTML file
# with open('website/index.html', 'r', encoding='utf-8') as file:
#     html = file.read()

# # Parse the HTML
# soup = BeautifulSoup(html, 'html.parser')

# # Create a new link tag
# link_tag = soup.new_tag('link')
# link_tag.attrs['rel'] = 'stylesheet'
# link_tag.attrs['href'] = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'

# # Add the link tag to the head
# soup.head.append(link_tag)

# # Find and remove all <span> tags with class 'titlemark'
# for tag in soup.find_all('span', {'class': 'titlemark'}):
#     tag.decompose()


#     # Find the <span> tag with class 'cmr-17x-x-143'
# h1tag = soup.find('span', {'class': 'cmr-17x-x-143'})


# # Find the span tag with class 'cmr-10'
# span_tag = soup.find('span', class_='cmr-10')

# # Check if the span tag exists
# if span_tag is not None:
#     # Get the parent p tag of the span tag
#     p_tag = span_tag.find_parent('p')

#     # Check if the p tag exists before changing its style
#     if p_tag is not None:
#         p_tag['style'] = 'width: 100%; box-sizing: border-box; text-align: center; font-size: 20px;'
#     else:
#         print("No parent p tag found for the span tag with class 'cmr-10'")
# else:
#     print("No span tag with class 'cmr-10' found")

# # Find the body tag
# body_tag = soup.find('body')

# # Check if the body tag exists before changing its style
# if body_tag is not None:
#     body_tag['style'] = 'font-size: 18px;'
# else:
#     print("No body tag found")


# # Find the table containing the rows
# table = soup.find('table',id="TBL-27")

# # Add style to the table tag
# # table['style'] = 'border: 1px solid black; padding: 10px;'

# # Find all tr tags within the table
# rows = table.find_all('tr')

# # Add style to each tr tag
# for row in rows:
#     row['style'] = 'border: 1px solid black; padding: 10px;'




# # Find the table with id 'TBL-3'
# table = soup.find('table', id='TBL-3')

# # Check if the table exists before changing its style
# if table is not None:
#     # Add style to the table tag to take full width
#     table['style'] = 'border: 1px solid black; padding: 10px; width: 100%;'

#     # Find all p tags within the table
#     p_tags = table.find_all('p')

#     # Add style to each p tag to center the text
#     for p_tag in p_tags:
#         p_tag['style'] = 'width: 100%; box-sizing: border-box; text-align: center;'
# else:
#     print("No table with id 'TBL-3' found")



# # Find the table with id 'TBL-24'
# table = soup.find('table', id='TBL-24')

# # Check if the table exists before changing its style
# if table is not None:
#     # Find all td tags within the table
#     td_tags = table.find_all('td')

#     # Add style to each td tag
#     for td_tag in td_tags:
#         if td_tag.text.strip():  # Check if the td tag contains some value
#             td_tag['style'] = 'border: 1px solid black; padding: 10px; margin: 10px;'
# else:
#     print("No table with id 'TBL-24' found")



# # Find the table with id 'TBL-27'
# table = soup.find('table', id='TBL-27')

# # Check if the table exists before changing its style
# if table is not None:
#     # Find all td tags within the table
#     td_tags = table.find_all('td')

#     # Add style to each td tag
#     for td_tag in td_tags:
#         if td_tag.text.strip():
#             td_tag['style'] = 'border: 1px solid black; padding: 10px; margin: 10px;'
# else:
#     print("No table with id 'TBL-27' found")    





# # Find all h3 tags with class 'sectionHead'
# sectionHeads = soup.find_all('h3', class_='sectionHead')

# # Add style to each h3 tag
# for head in sectionHeads:
#     head['style'] = 'font-size: 24px;'


















# # Modify the style attribute to set the font size and text alignment
# h1tag['style'] = 'font-size: 50px;  display: block;'


# # Write the modified HTML back to the file
# with open('website/index.html', 'w', encoding='utf-8') as file:
#     file.write(str(soup))
