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
with open('website/index.html', 'r') as file:
    html = file.read()

# Replace the images with FontAwesome icons
for image, icon in icon_mapping.items():
    html = re.sub(r'<img src="{}" alt="x  " >'.format(image), icon, html)

# Write the modified HTML back to the file
with open('website/index.html', 'w') as file:
    file.write(html)
