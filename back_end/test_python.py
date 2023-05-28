import os
from flask import Flask

from lxml import objectify, etree as ET
from random import randint
import csv
import sys
import jiraPostContentImport
import num_of_content

from pathlib import Path

app = Flask(__name__)

# def recursive remove


def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()

# test api route


@app.route("/test_function_python")
def test_function():
    return "test successfull"


# DL the content import to run the script for the number of content
@app.route("/content_import_sftp_filename/<cInstance>/<environment>/<ldapUsername>/<ldapPassword>")
def test_content_import_sftp_filename(cInstance, environment, ldapUsername, ldapPassword):
    print("bash runscript_ssh.sh " + cInstance +
          " " + ldapUsername + " " + ldapPassword)
    os.system("bash runscript_ssh.sh " + cInstance +
              " " + environment + " " + ldapUsername + " '" + ldapPassword + "'")

    # chieck how many files have been downloaded
    list_of_files = os.listdir("runtime-" + str(cInstance))
    if len(list_of_files) == 1:
        rmdir(Path("runtime-" + cInstance + "/"))
        return str(list_of_files[0])
    else:
        rmdir(Path("runtime-" + cInstance + "/"))
        return "Either no or more than one standart client feeds were found"


# DL the content import to run the script for the number of content
@app.route("/content_import_sftp/<cInstance>/<environment>/<ldapUsername>/<ldapPassword>")
def test_content_import_sftp(cInstance, environment, ldapUsername, ldapPassword):
    # print("bash runscript_ssh.sh " + cInstance +
    #       " " + ldapUsername + " " + ldapPassword)
    os.system("bash runscript_ssh.sh " + cInstance +
              " " + environment + " " + ldapUsername + " '" + ldapPassword + "'")

    # chieck how many files have been downloaded
    list_of_files = os.listdir("runtime-" + str(cInstance))
    if len(list_of_files) == 1:
        content_count = num_of_content.SFTP_content_count(
            "runtime-" + cInstance + "/" + str(list_of_files[0]))
        rmdir(Path("runtime-" + cInstance + "/"))
        return content_count
    else:
        rmdir(Path("runtime-" + cInstance + "/"))
        return "Either no or more than one standart client feeds were found"


@app.route("/jiraapi/<instance>/<cluster>/<environment>/<source>/<feedFileName>/<fingerprint>/<expectedNumContent>/<typesOfInput>/<displayCode>/<moderate>/<contentCodes>/<sfCase>/<minesweeper>")
def test_jira_api(instance, cluster, environment, source, feedFileName, fingerprint, expectedNumContent, typesOfInput, displayCode, moderate, contentCodes, sfCase, minesweeper):
    print(instance + " " + cluster + " " + environment + " " + source + " " + feedFileName + " " + fingerprint + " " + expectedNumContent +
          " " + typesOfInput + " " + displayCode + " " + moderate + " " + contentCodes + " " + minesweeper + " " + sfCase)
    return jiraPostContentImport.jiraPostContentImp(instance, cluster, environment, source, feedFileName, fingerprint, expectedNumContent, typesOfInput, displayCode, moderate, contentCodes, sfCase, minesweeper)


if __name__ == "__main__":
    app.run(debug=True)
