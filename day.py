import calendar
import datetime

def today_date():
    now = datetime.datetime.now()
    date_row = datetime.datetime.today()
    week_now = calendar.day_name[date_row.weekday()]
    month_now = now.month
    day_now = now.day

    month =['january','february','march','april','may','june','july','august','sepetember','octumber','november','december',]
    ordinals =['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',]
    print( f'today is {week_now},{month[month_now-1]}the {ordinals[day_now-1]}')
    print(now)

