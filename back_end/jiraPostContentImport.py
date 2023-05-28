import requests
import json
import os

# inputs


def jiraPostContentImp(instance, cluster, environment, source, feedFileName, fingerprint, expectedNumContent, typesOfInput, displayCode, moderate, contentCodes, sfCase, minesweeper):

    # input preparation
    if environment == "Production":
        environment = "prod"
    elif environment == "Staging":
        environment = "stg"

    if source == "Option 1":
        source = "New Client (external)"
    elif source == "Option 2":
        source = "PWR"
    elif source == "Option 3":
        source = "BV"

    if cluster == "c7":
        if environment == "prod":
            baseSFTPurl = "https://sftp7.bazaarvoice.com"
        else:
            baseSFTPurl = "https://sftp7-stg.bazaarvoice.com"
    else:
        if environment == "prod":
            baseSFTPurl = "https://sftp.bazaarvoice.com"
        else:
            baseSFTPurl = "https://sftp-stg.bazaarvoice.com"

    if fingerprint == "none":
        fingerprint = "N/A"

    if environment == "prod":
        asssignTo = "5fac7ed514da2600684fa128"  # content ops
    else:
        asssignTo = "5f92f6ac6bc6340068ecdc9c"  # EL2

    url = "https://bazaarvoice.atlassian.net"  # /rest/api/3/issue/
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project": {
                "key": "EL2"
            },
            "issuetype": {
                "name": "Request"
            },
            "assignee": {  # assign to content ops
                "accountId": "{}".format(asssignTo)
            },
            "customfield_10225": {  # custom field for request type
                # enter your request type
                "value": "Import - Native / Helpfulness / Fingerprint Content"
            },
            "customfield_10314": {  # custom field for reported team
                "value": "Client Delivery - EMEA"
            },
            # enter your summary
            "summary": "{}({}@{}) | Content import (Jira API test ticket)".format(instance, cluster, environment),
            "description": {
                "version": 1,
                "type": "doc",
                "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Service Request - Import Content",
                                    "marks": [
                                        {
                                            "type": "link",
                                            "attrs": {
                                                "href": "https://bazaarvoice.atlassian.net/wiki/display/DEV/Service+Request+-+Import+Content"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                    {
                            "type": "table",
                            "attrs": {
                                "isNumberColumnEnabled": False,
                                "layout": "default",
                                "localId": "9014c8f9-9724-42a0-8fd2-1079fa5a5062"
                            },
                            "content": [
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Client",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Client instance field
                                                            "text": "{}".format(instance)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Environment",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Environment field
                                                            "text": "{}".format(environment)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Source",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Source field
                                                            "text": "{}".format(source)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Feed File",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Feed file
                                                            "text": "{}/{}/native/{}".format(baseSFTPurl, instance, feedFileName),
                                                            "marks": [
                                                                {
                                                                    "type": "link",
                                                                    "attrs": {
                                                                        "href": "{}/{}/native/{}".format(baseSFTPurl, instance, feedFileName)
                                                                    }
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Fingerprint/Iovation File",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Fingerprint/lovation file
                                                            "text": "{}".format(fingerprint)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Expected # of content",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Expected # of content
                                                            "text": "{}".format(expectedNumContent)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Included content types",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Content types
                                                            "text": "{}".format(typesOfInput)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Display code",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Display code
                                                            "text": "{}".format(displayCode)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Moderate (new)?",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Moderate (new)
                                                            "text": "{}".format(moderate)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Content Codes",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # content codes
                                                            "text": "{}".format(contentCodes)
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Content Ops Approval",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": []  # Content ops approval
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "SFCase(s), SOW",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # SF case
                                                            "text": "{}".format(sfCase),
                                                            "marks": [
                                                                {
                                                                    "type": "link",
                                                                    "attrs": {
                                                                        "href": "{}".format(sfCase)
                                                                    }
                                                                }
                                                            ]
                                                        },
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Minesweeper Result",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            # Minesweaper results
                                                            "text": "https://minesweeper.prod.bazaarvoice.com/results/{}".format(minesweeper),
                                                            "marks": [
                                                                {
                                                                    "type": "link",
                                                                    "attrs": {
                                                                        "href": "https://minesweeper.prod.bazaarvoice.com/results/{}".format(minesweeper)
                                                                    }
                                                                }
                                                            ]
                                                        },
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Client Provided Import Files",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Attached below"  # client provided import files
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": " "
                                }
                            ]
                    },
                    {
                            "type": "heading",
                            "attrs": {
                                "level": 4
                            },
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Moderation Config Overrides"
                                }
                            ]
                    },
                    {
                            "type": "table",
                            "attrs": {
                                "isNumberColumnEnabled": False,
                                "layout": "default",
                                "localId": "01b32601-45a5-4faa-bb34-f099d36ca1da"
                            },
                            "content": [
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Ratings Only Approval Max",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "50 characters"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Optimistic Publishing",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "(NO or YES)"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": " "
                                }
                            ]
                    },
                    {
                            "type": "heading",
                            "attrs": {
                                "level": 4
                            },
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Processing Overrides"
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "(only need to enter a value if you want to override the default action)",
                                    "marks": [
                                        {
                                            "type": "em"
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "table",
                            "attrs": {
                                "isNumberColumnEnabled": False,
                                "layout": "default",
                                "localId": "d2c2f4f8-7ce2-457c-aefb-bf2b14559b80"
                            },
                            "content": [
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Behavior",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Default",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Value",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Import Helpfulness",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "NO",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": []
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Import Media",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "YES",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": []
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "tableRow",
                                    "content": [
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "Import Catalog",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableHeader",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "YES",
                                                            "marks": [
                                                                {
                                                                    "type": "strong"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "tableCell",
                                            "attrs": {},
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": []
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": " "
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "EL2 Runbook - Import Content Feeds",
                                    "marks": [
                                        {
                                            "type": "link",
                                            "attrs": {
                                                "href": "https://bazaarvoice.atlassian.net/wiki/display/DEV/EL2+Runbook+-+Import+Content+Feeds"
                                            }
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "heading",
                            "attrs": {
                                "level": 3
                            },
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Additional Info",
                                    "marks": [
                                        {
                                            "type": "strong"
                                        }
                                    ]
                                }
                            ]
                    },
                    {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    # additional info
                                    "text": "This is a test ticket for Jira automation. Please ignore these tickets. For any additional info please contact either Carlos Diamond or Lukas Paskevicius",
                                    "marks": [
                                        {
                                            "type": "em"
                                        }
                                    ]
                                }
                            ]
                    }
                ]
            }
        }
    })

    response = requests.post(
        url + "/rest/api/3/issue/",
        headers=headers,
        data=payload,
        # auth=(os.environ.get('JIRA_EMAIL_BV'), os.environ.get(
        #     'JIRA_TOKEN_BV'))  # email and api token
        auth=("lukas.paskevicius@bazaarvoice.com", "ATATT3xFfGF0dm171fuE4wVxPe8Q3wGf63b13gHu5hxuS9qeB94KlxdXx2-3LU3XBV1WS5uamEPGki1orWdWBrbhkngl126BPj6Zw6-bykR-hHzAulmjKLo9i0dL5Nn2YdjzvPfUivW8prZPa2jk0wH6AkXgX5A58QHV2tfX0rcS9f8vXlB7XHs=DD85986E")  # email and api token
    )
    print(response.status_code)
    if response.status_code == 201:
        issue = response.json()
        issue_key = issue["key"]
        print(f"Issue created: {issue_key}")
        ticket = url + "/browse/" + issue_key
        print(f"Issue link: {ticket}")
        return ticket
    else:
        print("Error creating issue")
        print(response, response.json())
        return "error"
