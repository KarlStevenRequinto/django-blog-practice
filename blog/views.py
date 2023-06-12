from django.shortcuts import render
from datetime import date
# dummy data
all_posts = [
    {
        "slug": "emarson-bayang",
        "image": "emarson-bayang.jpeg",
        "date": date(2022, 7, 21),
        "name": "Emarson Bayang",
        "alias": "'Pinakapogi'",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure incidunt
            officiis facilis dolor hic dolores nostrum rem illum rerum facere quaerat
            necessitatibus nemo repellat, et asperiores beatae voluptatibus sunt
            exercitationem.
        """
    },
    {
        "slug": "uly-rico",
        "image": "uly-rico.png",
        "date": date(2023, 1, 22),
        "name": "Uylses Rico",
        "alias": "'The Boss Master'",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure incidunt
            officiis facilis dolor hic dolores nostrum rem illum rerum facere quaerat
            necessitatibus nemo repellat, et asperiores beatae voluptatibus sunt
            exercitationem.
        """
    },
    {
        "slug": "steven-escarlan",
        "image": "steven-escarlan.png",
        "date": date(2022, 12, 12),
        "name": "Steven Escarlan",
        "alias": "'Lodi Petmalu'",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure incidunt
            officiis facilis dolor hic dolores nostrum rem illum rerum facere quaerat
            necessitatibus nemo repellat, et asperiores beatae voluptatibus sunt
            exercitationem.
        """
    },
    {
        "slug": "justin-aaron-rombawa",
        "image": "justin-aaron-rombawa.jpeg",
        "date": date(2022, 8, 2),
        "name": "Justin Aaron Rombawa",
        "alias": "'Master Diyos Kamahalan'",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure incidunt
            officiis facilis dolor hic dolores nostrum rem illum rerum facere quaerat
            necessitatibus nemo repellat, et asperiores beatae voluptatibus sunt
            exercitationem.
        """
    }
]


def get_date(post):
    return post["date"]
# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-4:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
