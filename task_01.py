#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This determines the number of tables needed and total attendees."""


def get_party_stats(families, table_size=6):
    """This function tells you the # of guests and tables needed.

    Args:
        families (list): A list of lists containing a group of families and
            its members.
        table_size (int, optional):  The seating capacity per table. The
            default is 6 seats per table.

    Returns:
        Tuple. The total number of people attending and the total number of
        tables needed based on the seating capacity per table.  Families are
        anti-social and will not share tables with members with other
        families; each family requires its own table(s).

    Examples:

        >>> get_party_stats([['Jan'], ['Jess'], ['Jem', 'Jack', 'Janis']])
        (5, 3)

        >>> get_party_stats([['Jan'], ['Jess'], ['Jem', 'Jack', 'Janis']], 2)
        (5, 4)
    """
    tablesneeded = 0
    totalattendees = 0
    for groups in families:
        tablesneeded += -(-len(groups) // table_size)
        for dummy in groups:
            totalattendees += 1
    return totalattendees, tablesneeded
