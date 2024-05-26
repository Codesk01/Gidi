from bs4 import BeautifulSoup

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOFT NET</title>
    <link rel="stylesheet" href="index.css"> 
</head>
<body>
    <header>
        <h1>HOME</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#Subscription">Subscription</a></li>
            <li><a href="#About">About</a></li>
        </ul>
    </nav>
    <img width="340" height="auto" src="img 1.jpeg" alt="Image 1" class="responsive-image">
    <div class="profile-img">
        <img width="315" height="auto" src="img 7.jpeg" class="responsive-image">
    </div>
    <p>Better gaming, good HD streaming, and long-range distance.</p>
    <!-- More HTML code here -->
</body>
</html>
"""

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Example: Get the title of the page
title = soup.title.string
print("Title:", title)

# Example: Get all the <a> tags
links = soup.find_all('a')
for link in links:
    print("Link:", link['href'])
