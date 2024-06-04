from django.shortcuts import render
from .forms import ConcertFilterForm
from .models import Concerts
from bs4 import BeautifulSoup
import re
import requests
from django.contrib import messages

# Create your views here.
def the_table(request):

    if not Concerts.objects.exists():
        add_concerts()

    reset_filters = request.GET.get('reset_filters', None) # посмотреть что делает этот метод
    concerts = Concerts.objects.all()
    my_form = ConcertFilterForm(request.GET)


    if reset_filters:
        concerts = Concerts.objects.all()
    else:
        filter_kwargs = {}
        for field in ['county', 'city', 'month', 'week_day', 'day_number', 'year', 'address', 'exact_time']:
            value = request.GET.get(field)
            if value:
                if field in ['day_number']:
                    filter_kwargs[f"{field}"] = value
                elif field in ['exact_time']:
                    filter_kwargs[f"{field}__exact"] = value
                else:
                    filter_kwargs[f"{field}__icontains"] = value

        concerts = concerts.filter(**filter_kwargs)

    return render(request, 'main_table/table_template.html',
                  {'concerts': concerts, 'my_form': my_form})


def add_concerts():
    URL = "https://www.andreabocelli.com/tickets"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    all_info = soup.find_all("article", {"class": "m-gigs"})
    for info in all_info:
        for item in info.find_all("div", {"class": "m-gig-detail__description"}):
            new_item = item.text.strip() # убирает пробелы с начала и с конца

            lines = new_item.split('\n')
            date_time_info = [x.strip() for x in lines[0].split(',')]
            day_week = date_time_info[0]
            month_day_year = date_time_info[1].split()
            month = month_day_year[0]
            day_number = int(re.search(r'\d+', month_day_year[1]).group()) # напомнить что делает груп и почему именно такой шаблон
            year = int(month_day_year[2])
            time_12hr = date_time_info[2]
            exact_time = re.sub(r'(\d{2}):(\d{2})\s*(am|pm)',
                                lambda x: f"{int(x.group(1)) % 12 + (12 if x.group(3) == 'pm' else 0)}:{x.group(2)}:00",
                                time_12hr) # про эту строчку тоже напомнить
            address = lines[1].strip()
            city_country = [x.strip() for x in re.split(r',|.', lines[2])]
            city = city_country[0]
            country = city_country[1]

            try:
                concert = Concerts(
                    county=country,
                    city=city,
                    month=month,
                    week_day=day_week,
                    day_number=day_number,
                    year=year,
                    address=address,
                    exact_time=exact_time
                )
                concert.save()
            except Exception as e:
                raise AssertionError("Could not create concert", e)
