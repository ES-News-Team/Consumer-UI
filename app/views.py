from flask import redirect, render_template
from app import consumer_ui_service


data_pet = {
    "window_title": "Pets News",
    "news": [
        {   
            "news_link_img": "https://thiscatdoesnotexist.com/",
            "news_title": "News 1",
            "new_content": """“In the long run, we’re going to make it happen. ’ ‐It’s an incredibly cool way of seeing the future. I’m proud to announce that I'm starting an internship and will continue to pursue my passion for programming. ‡ “As long as I continue to pursue my passion for programming, I will continue to pursue my passion for programming. I’m proud to announce that I'm starting an internship and will continue to pursue my passion for programming. ‡ The Beginning of Programming

I hope to get to know you! I hope you’ll be able to join us!

Thanks for coming and"""
        },

        {
            "news_link_img": "https://thiscatdoesnotexist.com/",
            "news_title": "News 2",
            "new_content": """“In the long run, we’re going to make it happen. ’ ‐It’s an incredibly cool way of seeing the future. I’m proud to announce that I'm starting an internship and will continue to pursue my passion for programming. ‡ “As long as I continue to pursue my passion for programming, I will continue to pursue my passion for programming. I’m proud to announce that I'm starting an internship and will continue to pursue my passion for programming. ‡ The Beginning of Programming

I hope to get to know you! I hope you’ll be able to join us!

Thanks for coming and"""
        }
    ]
}


data_art = {
    "window_title": "Art News",
    "news": [
        {   
            "news_link_img": "https://thisartworkdoesnotexist.com/",
            "news_title": "News 1",
            "new_content": """
            A couple of weeks ago 
            I wrote about the development of 
            the new iPhone X, which is scheduled 
            to launch in the first few weeks. As 
            it turns out, the iPhone X comes equipped 
            with a fully wireless charging cable and is
             very well tuned to the performance of the X. 
             This is certainly a nice step forward. I wanted to give you some information on the current iPhone X, as well as what the specifications are"""
    },
    {   
            "news_link_img": "https://thisartworkdoesnotexist.com/",
            "news_title": "News 2",
            "new_content": """
            A couple of weeks ago 
            I wrote about the development of 
            the new iPhone X, which is scheduled 
            to launch in the first few weeks. As 
            it turns out, the iPhone X comes equipped 
            with a fully wireless charging cable and is
             very well tuned to the performance of the X. 
             This is certainly a nice step forward. I wanted to give you some information on the current iPhone X, as well as what the specifications are"""
    },
    ]
}



data_sci = {
    "window_title": "Sci News",
    "news": [
        {   
            "news_link_img": "https://thischemicaldoesnotexist.com/",
            "news_title": "News 1",
            "new_content": """
            A couple of weeks ago 
            I wrote about the development of 
            the new iPhone X, which is scheduled 
            to launch in the first few weeks. As 
            it turns out, the iPhone X comes equipped 
            with a fully wireless charging cable and is
             very well tuned to the performance of the X. 
             This is certainly a nice step forward. I wanted to give you some information on the current iPhone X, as well as what the specifications are"""
    },
    {   
            "news_link_img": "https://thischemicaldoesnotexist.com/",
            "news_title": "News 2",
            "new_content": """
            A couple of weeks ago 
            I wrote about the development of 
            the new iPhone X, which is scheduled 
            to launch in the first few weeks. As 
            it turns out, the iPhone X comes equipped 
            with a fully wireless charging cable and is
             very well tuned to the performance of the X. 
             This is certainly a nice step forward. I wanted to give you some information on the current iPhone X, as well as what the specifications are"""
    },
    ]
}


@consumer_ui_service.route('/')
def index():
    return redirect('/pets')


@consumer_ui_service.route('/pets')
def pets_news():
    return render_template('listagem_noticias.html', **data_pet)


@consumer_ui_service.route('/artes')
def artes_news():
    return render_template('listagem_noticias.html', **data_art)

@consumer_ui_service.route('/ciencias')
def ciencia_news():
    return render_template('listagem_noticias.html', **data_sci)
    