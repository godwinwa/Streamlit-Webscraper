import streamlit as st
from skysports_news import news

#Page settings
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
	page_title=None,  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What sports are you interested in?',
    ('football', 'f1', 'boxing')
)

#Get news
sky_sports = news()
sky_sports_news = sky_sports.webscrape_site('https://www.skysports.com/{}'.format(add_selectbox))
sky_sports_news_header = sky_sports.get_news_headers(sky_sports_news, "news-top-story__headline-link")
amount_articles_list = sky_sports.get_amount_articles(sky_sports_news,"news-list-featured__link" )
sky_sports_news_list = sky_sports.get_news_headers(sky_sports_news, "news-list-featured__link", amount_articles_list)
amount_articles_headline = sky_sports.get_amount_articles(sky_sports_news,"news-list__headline-link" )
sky_sports_news_headline = sky_sports.get_news_headers(sky_sports_news, "news-list__headline-link", amount_articles_headline)
sky_sports_images = sky_sports.get_images(sky_sports_news)

#Header
st.header('News of the Day')
#Header centre
#st.markdown("<h1 style='text-align: center; color: white;'>A Bambelaars Creations</h1>", unsafe_allow_html=True)

#Display news
number_articles = 0
st.write(sky_sports_news_header[0])
link = sky_sports_news_header[1]
st.caption("Read the article [link](%s)" % link)
if add_selectbox == 'football':
    st.image(sky_sports_images['2'])
else:
    st.image(sky_sports_images['1'])
number_articles += 1

for i in range(len(sky_sports_news_list)):
    st.write(sky_sports_news_list[i][0])
    link = sky_sports_news_list[i][1]
    st.caption("Read the article [link](%s)" % link)
    #st.image(sky_sports_images[str(4+i)])
    number_articles += 1

for i in range(len(sky_sports_news_headline)):
    st.write(sky_sports_news_headline[i][0])
    link = sky_sports_news_headline[i][1]
    st.caption("Read the article [link](%s)" % link)
   # st.image(sky_sports_images[str(2+i)])
    number_articles += 1
st.write(number_articles, 'articles')

with st.expander("Source"):
     st.write("""
         The articles are scraped from Skysports
     """)
    
#Hide streamlit logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)