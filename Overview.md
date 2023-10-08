### Webscraping using BeautifulSoup

## Table of Contents

- [Introduction](#introduction)
- [Package/Library Selection](#package-library-selection)
- [Package/Library Details](#package-library-details)
- [Package/Library History](#package-library-history)
- [Reasons for Selection](#reasons-for-selection)
- [Impact on Learning](#impact-on-learning)
- [Overall Experience](#overall-experience)

## 1. Introduction <a name="introduction"></a>

Welcome to the Wiki for Web Scraping with BeautifulSoup. In this Wiki, we will explore the package/library used in the project, its purpose, functionalities, and more.

What is web scraping?
Web scraping is the process of gathering information from the Internet. Copying and pasting from some other websites is a form of web scraping. However, webscraping is typically considered as automation process.[4]

## 2. Package/Library Selection <a name="package-library-selection"></a>

For this project, I selected the following package/library:

Package/Library: Beautiful Soup (bs4).

### How to use it?

1. Before using BeautifulSoup, you need to install it.

```bash
pip install beautifulsoup4
```

2. In your Python script, import BeautifulSoup from the `bs4` package along with the `requests` library which is commonly used together:

```python
from bs4 import BeautifulSoup
import requests
```

3. Create a BeautifulSoup Object.
   To parse an HTML or XML document, create a BeautifulSoup object by passing the document content and a parser to the constructor. Example: [Creating BeautifulSoup object](#creating-BeautifulSoup-object)

4. Navigating the Document:
   You can navigate the document using various methods and properties provided by BeautifulSoup. Here are some common navigation methods:

   `soup.tag_name`: Access the first occurrence of a tag with a specific name.

   `soup.tag_name.string`: Access the text content of a tag.

   `soup.find('tag_name')`: Find the first occurrence of a specific tag.

   `soup.find_all('tag_name')`: Find all occurrences of a specific tag and return a list.

   `tag.parent`, `tag.next_sibling`, `tag.previous_sibling`: Navigate to the parent and siblings of a tag.

   `tag.get('attribute')`: Access the value of an attribute in a tag.

   `tag.contents`: Access the direct children of a tag as a list.

   `tag.descendants`: Iterate through all descendants of a tag. [1]

5. Extracting Data:
   Finally you can extract the data you are interested in:
   ```python
   # Extract the text content of the 'h1' tag
    h1_text = soup.h1.string
   ```

## 3. Package/Library Details <a name="package-library-details"></a>

Beautiful Soup (bs4) is a Python library used for parsing and navigating HTML and XML documents[1], while Requests (requests) is a library for making HTTP requests. [3] Together, they form a powerful combination for web scraping.
These libraries serve the purpose of extracting data from web pages by parsing their HTML content. [5]

They are commonly used for web scraping, data mining, and data extraction tasks. [5]

Beautiful Soup allows you to locate and manipulate HTML/XML elements.[1]

## Examples:

### EX1 Creating BeautifulSoup object <a name="creating-BeautifulSoup-object"></a>

```python
import requests
from bs4 import BeautifulSoup

    # Make an HTTP request

    response = requests.get('https://example.com')

    # Parse the HTML content

    soup = BeautifulSoup(response.text, 'html.parser')

```

### EX2 Prettify() to format document

The 'prettify()' method is used to format the document with proper indentation[1]

```python
print(soup.prettify())
```

### Output

```html
<html>
  <body>
    <p>Hello, World!</p>
  </body>
</html>
```

### EX3 `find()` and `find_all()` - searching for elements

`find()` returns the first matching element, and `find_all()` returns a list of all matching elements.[1]

```python
# Find the first 'p' element
first_p = soup.find('p')
print(first_p)

# Find all 'p' elements
all_p = soup.find_all('p')
print(all_p)

```

### Output:

```html
<p>Hello, World!</p>
[
<p>Hello, World!</p>
]
```

### EX4 Accessing tag attributes:

You can access attributes of a tag using dictionary-like notation.[1]

```python
tag = soup.find('p')
print(tag['class'])
```

### Output:

```css
['my-class']
```

### EX5 Navigating the document:

BeautifulSoup provides methods like `parent`, `next_sibling`, and `previous_sibling` to navigate the document tree.[1]

```py
body = soup.body
paragraph = body.p
next_paragraph = paragraph.next_sibling
```

### EX6 `get_text()` to extract text content

The `get_text()` method extracts the text content of a tag and its descendants.[1]

```py
text = soup.get_text()
print(text)
```

### Output

`Hello, World!`

## 4. Package/Library History <a name="package-library-history"></a>

Creation Date: Beautiful Soup was first released in 2004, the current release is Beautiful Soup 4.12.2 (April 7, 2023).[2]

## 5. Reasons for Selection <a name="reasons-for-selection"></a>

Initially, the name of the library was what got my interest. I selected Beautiful Soup after learning they are widely used and well-documented libraries for web scraping in Python.
They provide a simple and effective way to extract data from web pages.

## 6. Impact on Learning <a name="impact-on-learning"></a>

I already have experience web scraping using another language/framework such as Selenium in JS. Using python library to do similar tasks was interesing.
It enhanced my understanding of how to work with external libraries in Python.

## 7. Overall Experience <a name="overall-experience"></a>

I highly recommend this library to anyone involved in web scraping or data collection tasks. I found it is simpler than other libraries I've used when webscraping.
However, it also had limitations well. Initally, I tried web scraping from Amazon. It was challening as Amaznon's website is dynamic and loaded with JS. BeautifulSoup is primarily designed for parsing static or semi-static web pages.[5]
I will continue to use Beautiful Soup for simple data collection due to their reliability and ease of use.

### References

1. [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [Beautiful SOUP Homepage](https://www.crummy.com/software/BeautifulSoup/)
3. [Requests Documentation](https://docs.python-requests.org/en/latest/)
4. [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
5. [Selenium vs. BeautifulSoup in 2023: Which Is Better?](https://www.zenrows.com/blog/selenium-vs-beautifulsoup)
