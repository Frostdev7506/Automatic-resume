import re
import os

# Define the mapping between image names and FontAwesome icons
icon_mapping = {
    "Neeraj_Butola_Resume10x.png": '<i class="fab fa-github"></i>',
    "Neeraj_Butola_Resume11x.png": '<i class="fab fa-linkedin"></i>',
    "Neeraj_Butola_Resume12x.png": '<i class="fas fa-briefcase"></i>',
    "Neeraj_Butola_Resume13x.png": '<i class="fas fa-envelope"></i>',
    "Neeraj_Butola_Resume14x.png": '<i class="fas fa-phone"></i>',
}

# Read the HTML file
with open('website/index.html', 'r', encoding='ISO-8859-1') as file:
    html = file.read()

# Replace non-UTF-8 characters
html = html.encode('utf-8', errors='ignore').decode('utf-8')


# Replace the images with FontAwesome icons
for image, icon in icon_mapping.items():
    match = re.search(r'<img\s+src="{}"\s+alt="x\s*"\s*>'.format(image), html)
    if match:
        print(f"Found image: {match.group()}")
        html = re.sub(r'<img\s+src="{}"\s+alt="x\s*"\s*>'.format(image), icon, html)





# Write the modified HTML back to the file
with open('website/index.html', 'w') as file:
    file.write(html)
