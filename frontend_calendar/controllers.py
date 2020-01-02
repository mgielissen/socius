# -*- coding: utf-8 -*-

from datetime import datetime
import json
import pytz
from tzlocal import get_localzone
from calendar import HTMLCalendar

from odoo.http import Controller, route, request
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


def convert_to_real_datetime(
                            datetime_str,
                            tz,
                            dt_format_str=DEFAULT_SERVER_DATETIME_FORMAT,
                            as_str=False,
                            display_dt_format_str='%d.%m.%Y %H:%M'):
    """ display_dt_format_str is default european datetime format """
    if tz:
        timezone = pytz.timezone(tz)
    else:

        # get local timezone
        timezone = get_localzone()
    str_time = datetime.strptime(str(datetime_str), dt_format_str)
    datetime_obj = pytz.UTC.localize(str_time)
    real_datetime = datetime_obj.astimezone(timezone)
    if as_str:
        real_datetime = real_datetime.strftime(display_dt_format_str)
    return real_datetime


class CalendarHTMLwithInfos(HTMLCalendar):

    def __init__(self, firstweekday=0, data=None):
        self.firstweekday = firstweekday  # 0 = Monday, 6 = Sunday
        if data is None:
            data = {}
        self.data = data

    def formatday(self, day, weekday):
        """
        Return a day with corresponding infos from self.data for a table cell.
        """
        if day == 0:
            # day outside month
            return '<td align="center" valign="top" class="outside-month"><div class="td-inner">&nbsp;</div></td>'
        else:
            if weekday in [5, 6]:
                css_class = 'weekend-days'
            else:
                css_class = 'working-days'
            return '<td align="center" valign="top" class="%s"><div class="td-inner">%d%s</div></td>' % (css_class, day, self.data.get(day, '&nbsp;'))

    # def formatmonth(self, theyear, themonth, withyear=True):
    #     """
    #     Return a formatted month as a table.
    #     """
    #     v = []
    #     a = v.append
    #     a('<table border="0" cellpadding="0" cellspacing="0" width="70%%">')
    #     a('\n')
    #     a(self.formatmonthname(theyear, themonth, withyear=withyear))
    #     a('\n')
    #     a(self.formatweekheader())
    #     a('\n')
    #     for week in self.monthdays2calendar(theyear, themonth):
    #         a(self.formatweek(week))
    #         a('\n')
    #     a('</table></head></html>')
    #     a('\n')
    #     return ''.join(v)


class PublicCalendar(Controller):

    @route('/web/public-calendar/', auth='public', website=True, csrf=False)
    def index(self, **kw):
        form = request.httprequest.form
        self.direction = form.get('direction')
        self._get_month_year()
        self._get_datetime_range()
        self._event_s_e_map = {
            'event.event':
                {'start': 'date_begin', 'end': 'date_end'},
            'calendar.event':
                {'start': 'start_datetime', 'end': 'stop_datetime'},
        }
        events = self._get_events('event.event')
        calendar_events = self._get_events('calendar.event')
        self._day_events_html_map = {}
        self.create_day_events_html_map('event.event', events)
        self.create_day_events_html_map('calendar.event', calendar_events)
        html_calendar = CalendarHTMLwithInfos(data=self._day_events_html_map)
        html_calendar_code = html_calendar.formatmonth(self.year, self.month)
        html_calendar_code = html_calendar_code.replace('class="month"', 'class="month center"')
        if not self.direction:
            # view is called for the first time and render entire template
            return request.render(
                                'frontend_calendar.public_calendar_view',
                                {
                                    'month': self.month,
                                    'year': self.year,
                                    'html_calendar_code': html_calendar_code,
                                    'direction': self.direction
                                }
                                )
        else:
            # render only calendar view using ajax
            return json.dumps(
                                {
                                    'month': self.month,
                                    'year': self.year,
                                    'html_calendar_code': html_calendar_code
                                }
                            )

    def _get_month_year(self):
        if self.direction == 'next':
            self.month += 1
        elif self.direction == 'previous':
            self.month -= 1
        else:
            # take current month and year
            now = datetime.now()
            self.month = now.date().month
            self.year = now.date().year
        if self.month == 0:
            self.month = 12
            self.year -= 1
        elif self.month == 13:
            self.month = 1
            self.year += 1

    def _get_datetime_range(self):
        if self.month == 12:
            next_month = 1
            next_year = self.year + 1
        else:
            next_month = self.month + 1
            next_year = self.year
        start_datetime = datetime(self.year, self.month, 1)
        end_datetime = datetime(next_year, next_month, 1)
        self.start_datetime_str = start_datetime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        self.end_datetime_str = end_datetime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

    def _get_events(self, event_model_name):
        event_model = request.env[event_model_name]
        events = event_model.sudo().search(
                    [
                        (self._event_s_e_map[event_model_name]['start'], '>=', self.start_datetime_str),
                        (self._event_s_e_map[event_model_name]['end'], '<=', self.end_datetime_str)
                    ], order=self._event_s_e_map[event_model_name]['start']
                    )
        return events

    def create_day_events_html_map(self, event_model_name, events):
        tf = '%H:%M'
        el_1 = u'<div class="bold %s">%s %s<div>'
        href_el = '<a class="forPrintHidden" href="%s">&swarr;</a>'
        el_2 = u'<div>%s-%s<div>'



        # cancelled_st = 'style="color:red"'
        # present_st = 'style="color:#12536d"'
        # absent_st = 'style="color:#ff8080"'

        for e in events:
            start_str = getattr(e, self._event_s_e_map[event_model_name]['start'], None)
            # ogi: by reccurent calendar events can occur that start is missing !?
            if start_str:
                e_start_datetime = convert_to_real_datetime(start_str, None)
                day = e_start_datetime.day
                # it can be more events in a single day
                more_events_in_day = False
                if day not in self._day_events_html_map:
                    # first found event in day and initialize self._day_events_html_map[day]
                    first_event_in_day = True
                    self._day_events_html_map[day] = u'<div class="day-data">'
                    # extra_cl = 'pT10'
                    extra_cl = ''
                    line = '<div>____________</div>'
                else:
                    first_event_in_day = False
                    more_events_in_day = True
                    # extra_cl = 'pT10'
                    extra_cl = ''
                    line = '<div>____________</div>'
                self._day_events_html_map[day] += line
                if hasattr(e, 'website_url'):
                    e_url = e.website_url
                else:
                    e_url = '../#id=%d&view_type=form&model=%s' % (e.id, event_model_name)
                self._day_events_html_map[day] += el_1 % (extra_cl, e.name, href_el % e_url)
                self._day_events_html_map[day] += el_2 % \
                    (
                        getattr(e, self._event_s_e_map[event_model_name]['start'], ''),
                        getattr(e, self._event_s_e_map[event_model_name]['end'], '')
                    )
                if (more_events_in_day and not first_event_in_day) or first_event_in_day:
                    # assuming that there are maximal two events in day:
                    self._day_events_html_map[day] += '<div class="pB10"></div>'
                self._day_events_html_map[day] += '</div>'
