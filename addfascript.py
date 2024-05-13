from bs4 import BeautifulSoup

# Read the HTML file
with open('website/index.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Create a new link tag
link_tag = soup.new_tag('link')
link_tag.attrs['rel'] = 'stylesheet'
link_tag.attrs['href'] = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'

# Add the link tag to the head
soup.head.append(link_tag)

# Write the modified HTML back to the file
with open('website/index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
