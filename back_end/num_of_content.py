from lxml import objectify, etree as ET
from random import randint
import csv
import sys


def SFTP_content_count(filepath):

    # -- Define the root --#

    it = ET.iterparse(filepath, encoding="utf-8")
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    root = it.root

    # -- Total number of reviews -- #

    print("All reviews: ", len(root.findall('.//Review')))

    # -- Total number of questions -- #

    print("All questions: ", len(root.findall('.//Question')))

    # -- Total number of answers -- #

    print("All answers: ", len(root.findall('.//Answer')))

    # -- Total number of content -- #

    print("Total number of content: ", len(root.findall('.//Answer')) +
          len(root.findall('.//Question')) + len(root.findall('.//Review')))

    # return_str = "All reviews : " + len(root.findall('.//Answer')) + "\nAll questions : " + len(
    #     root.findall('.//Question')) + "\nAll answersns : " + len(root.findall('.//Answer')) + "\nTotal number of content : " + len(root.findall('.//Answer')) +
    # len(root.findall('.//Question')) + len(root.findall('.//Review'))

    # return_str = "All reviews : " + \
    #     str(len(root.findall('.//Review'))) + "\nAll questions : " + \
    #     str(len(root.findall('.//Question'))) + "\nAll answers : " + \
    #     str(len(root.findall('.//Answer'))) + "\nTotal count : " + \
    #     str(len(root.findall('.//Answer')) +
    #         len(root.findall('.//Question')) + len(root.findall('.//Review')))

    return str(len(root.findall('.//Answer')) + len(root.findall('.//Question')) + len(root.findall('.//Review')))
