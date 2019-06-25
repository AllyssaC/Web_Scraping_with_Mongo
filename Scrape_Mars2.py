    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:

def scrape():

    # import all dependencies
    import time
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    import numpy as np
    from selenium import webdriver


    # In[14]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    # Mac Users
    #!which chromedriver
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #browser = Browser('chrome', **executable_path, headless=False)


    # NASA MARS NEWS
    # 
    # 

    # In[15]:


    # URL of page to be scraped

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[16]:


    #html object
    html = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())


    # In[17]:


    #Collect the latest News Title and Paragraph Text. Assign text to a variable that you can reference later
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    print(news_title)
    print(news_p)


    # JPL Mars Space Featured Image

    # In[18]:


    #* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    #Use splinter to navigate the site and find the image url for the current Featured Mars Image and 
    #assign the url string to a variable called `featured_image_url`
    
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)


    # In[8]:


    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[19]:

    time.sleep(10)
    browser.click_link_by_partial_text('FULL IMAGE')


    # In[20]:

    time.sleep(10)
    browser.click_link_by_partial_text('more info')


    # In[21]:


    main_url = 'https://www.jpl.nasa.gov'
    new_html = browser.html
    new_soup = BeautifulSoup(new_html, 'html.parser')
    temp_img_url = new_soup.find('img', class_='main_image')
    back_half_img_url = temp_img_url.get('src')

    featured_image_url = main_url + back_half_img_url

    print(featured_image_url)


    # Mars Weather

    # In[ ]:


    #Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en)
    #and scrape the latest Mars weather tweet from the page
    #Save the tweet text for the weather report as a variable called `mars_weather


    # In[22]:


    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)


    # In[23]:


    html_weather = browser.html
    soup = BeautifulSoup(html_weather, 'html.parser')
    tweets = soup.find_all('div', class_='js-tweet-text-container')
    for tweet in tweets:
        Mars_weather_tweets = tweet.find('p').text
        if 'Insight' in Mars_weather_tweets:
            print (Mars_weather_tweets)
            break
        else:    
            pass

        Mars_weather_tweets


    # Mars Facts

    # In[24]:


    #Visit the Mars Facts webpage [here](https://space-facts.com/mars/) 
    #and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    #Pandas to convert the data to a HTML table string.
    Mars_facts_url = 'https://space-facts.com/mars/'
    #Pandas to read and parse
    Mars_facts = pd.read_html(Mars_facts_url)
    #Create dataframe for facts
    Mars_df = Mars_facts[0]
    Mars_df.columns = ['Descriptor','Value']
    Mars_df.set_index('Descriptor', inplace=True)
    mars_dict = {}
    for row in Mars_df.iterrows():
        mars_dict[row[0][:-1]] = row[1][0]


    # Mars Hemispheres

    # In[ ]:


    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    # * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
    # * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


    # In[25]:


    #Use Splinter
    
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)


    # In[26]:


    #HTML Object
    hemispheres_html = browser.html
    #Parse with BeautifulSoup
    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')


    # In[27]:


    hemi_info = hemispheres_soup.find_all('div', class_="description")
    for hemi in hemi_info:
        print(hemi.find("a")["href"])


    # In[28]:


    #Create a list w/ links for each hemisphere
    hemispheres_links = []
    hemi_links = hemispheres_soup.find_all('h3')

    for hemi in hemi_links:
        hemispheres_links.append(hemi.text)

    hemispheres_links


    # In[29]:


    # Parse html file with BeautifulSoup

    mars_hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')


    # In[30]:


    # Find hemisphere image link and title
    mars_hemispheres = mars_hemispheres_soup.find_all('div', class_='description')
    mars_hemispheres


    # In[31]:


    #Store main urls
    MainURL = 'https://astrogeology.usgs.gov'
    #Initialize hemisphere_image_urls list
    hemisphere_image_urls = []
    # Loop through each link of hemispheres on page
    for image in mars_hemispheres:
        hemisphere_url = image.find('a', class_='itemLink')
        hemisphere = hemisphere_url.get('href')
        hemisphere_link =MainURL + hemisphere
        print(hemisphere_link)

        hemisphere_image_urls.append(hemisphere_link)






    # In[32]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', headless=False)

    hemi_page = hemisphere_image_urls[0]
    browser.visit(hemi_page)


    # In[33]:


    mars_hemispheres_soup = BeautifulSoup(browser.html, 'html.parser')
    mars_hemispheres_soup


    # In[34]:


    #Store main urls
    MainURL = 'https://astrogeology.usgs.gov'
    Image=mars_hemispheres_soup.find("img", class_="wide-image")["src"]
    Title=mars_hemispheres_soup.find("h2", class_="title")
    FullImage = MainURL + Image
    Title, FullImage


    # In[35]:


   

    hemi_page1 = hemisphere_image_urls[1]
    browser.visit(hemi_page1)
    mars_hemispheres_soup1 = BeautifulSoup(browser.html, 'html.parser')
    Image1=mars_hemispheres_soup1.find("img", class_="wide-image")["src"]
    FullImage1 = MainURL + Image1
    Title1=mars_hemispheres_soup1.find("h2", class_="title")
    Title1, FullImage1


    # In[36]:


   
    hemi_page2 = hemisphere_image_urls[2]
    browser.visit(hemi_page2)
    mars_hemispheres_soup2 = BeautifulSoup(browser.html, 'html.parser')
    Image2=mars_hemispheres_soup2.find("img", class_="wide-image")["src"]
    FullImage2 = MainURL + Image2
    Title2=mars_hemispheres_soup2.find("h2", class_="title")
    Title2, FullImage2


    # In[37]:




    hemi_page3 = hemisphere_image_urls[3]
    browser.visit(hemi_page3)
    mars_hemispheres_soup3 = BeautifulSoup(browser.html, 'html.parser')
    Image3 = mars_hemispheres_soup3.find("img", class_="wide-image")["src"]
    FullImage3 = MainURL + Image3
    Title3=mars_hemispheres_soup3.find("h2", class_="title")
    Title3, FullImage3


    # In[38]:


    All_Images = [FullImage, FullImage1, FullImage2, FullImage3]
    All_Images


    # In[39]:


    All_Titles = [Title, Title1, Title2, Title3]
    All_Titles


    mars_data = {
    "Mars_News_Title": news_title,
    "Mars_News": news_p,
    "Mars_Featured_Image": featured_image_url,
    "Mars_Twitter_Weather": Mars_weather_tweets,
    "Mars_Facts": mars_dict,
    "Mars_Hemispheres_Links": hemispheres_links,
    "Mars_Hemispheres_Images": All_Images,
    "Mars_Hemispheres_Titles": All_Titles

    }

    browser.quit()

    return mars_data
