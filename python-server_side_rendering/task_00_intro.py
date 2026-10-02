#!/usr/bin/python3
"""Generate personalized invitation files from a template.

This module provides the generate_invitations function, which fills a
template containing placeholders with the data of each attendee and
writes one output file per attendee.
"""
import logging
import os

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Create the files output_1.txt, output_2.txt, ... from a template.

    The template is a string with the placeholders {name}, {event_title},
    {event_date} and {event_location}. Attendees is a list of dictionaries.
    A missing or None value is replaced with "N/A". Invalid or empty input
    is logged as an error and no file is generated.
    """
    if not isinstance(template, str):
        logging.error("Invalid input type: template must be a string, "
                      "got %s.", type(template).__name__)
        return
    if (not isinstance(attendees, list) or
            not all(isinstance(item, dict) for item in attendees)):
        logging.error("Invalid input type: attendees must be a list of "
                      "dictionaries.")
        return
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))
        filename = "output_{}.txt".format(index)
        if os.path.exists(filename):
            logging.warning("%s already exists and will be overwritten.",
                            filename)
        try:
            with open(filename, "w") as file:
                file.write(content)
        except OSError as error:
            logging.error("Could not write %s: %s", filename, error)
