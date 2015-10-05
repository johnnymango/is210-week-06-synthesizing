#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Email Appointment Lists."""


def prepare_email(appointments):
    """This function creates an email list of clients and their appointments.

    Args:
        appointments (list): A list of tuples containing the client name and
        their appointment dates.

    Returns:
        List: A list of strings formatted to include the client name and date in
        the body of the string (email body).

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    emaillst = []
    for items in appointments:
        emaillst.append('Dear {},\nI look forward to meeting with you on {'
                        '}.\nBest,' '\nMe'.format(*items))
    return emaillst
