import xml.etree.ElementTree as et
import dateutil.parser
import os
"""
Parsing script. Reads the list file to create the directory structure and parse folder info,
then reads the log file to create the file lists and parse file info, as well as the revisions
"""

code_ext = [".py", ".java", ".js"]
URL = "https://subversion.ews.illinois.edu/svn/sp17-cs242"

# create relative links
site_root = os.path.realpath(os.path.dirname(__file__))
svn_list = os.path.join(site_root, "data", "svn_list.xml")
svn_log = os.path.join(site_root, "data", "svn_log.xml")


def parse_files():
    """
    Main parsing function. Returns a dict of the directory, along with each directory having a dict of files nested
    inside it, and each file having a revisions dict nested inside it
    """

    list = svn_list
    log = svn_log
    dir = {}

    # ElementTree traversal from http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree
    tree = et.parse(list)
    root = tree.getroot()

    for list_entry in root.iter('entry'):

        name = list_entry.find("name").text
        is_dir = list_entry.get("kind") == "dir"
        commit = list_entry.find("commit")
        author = commit.find("author").text
        date = dateutil.parser.parse(commit.find("date").text)
        version = commit.get("revision")

        # if not file
        if not author or not date or not version:
            continue

        dir_path = name.split("/")
        curr_dir = dir

        # add blank dictionaries for subdirectories
        for directory in dir_path[:-1]:

            if directory in curr_dir:
                curr_dir = curr_dir[directory]
            else:
                curr_dir[directory] = {}
                curr_dir = curr_dir[directory]

        # parse directory info
        if author and date and version:
            curr_dir[dir_path[-1]] = {"author": author, "date": date, "version": version,
                                      "revisions": [], "is_directory": is_dir}

        # get size
        if list_entry.find("size") is not None:
            curr_dir[dir_path[-1]]["size"] = list_entry.find("size").text

    tree = et.parse(log)
    root = tree.getroot()
    for log_entry in root.iter('logentry'):

        msg = log_entry.find("msg").text
        date = dateutil.parser.parse(log_entry.find("date").text)
        version = log_entry.get("revision")
        author = log_entry.find("author").text

        # check if valid statement
        if not msg:
            continue

        paths = log_entry.find("paths")

        for path in paths.findall("path"):
            action = path.get("action")

            # ignore deleted file paths
            if action == "D":
                continue

            dir_path = path.text.split("/")
            curr_dir = dir

            # create any missing subdirectories
            for directory in dir_path[2:-1]:

                if directory in curr_dir:
                    curr_dir = curr_dir[directory]
                else:
                    curr_dir[directory] = {}
                    curr_dir = curr_dir[directory]

            file_name = dir_path[-1]

            if file_name not in curr_dir:
                continue

            # cut off files from directory list
            if "is_directory" in curr_dir[file_name]:
                is_dir = curr_dir[file_name]["is_directory"]
                del curr_dir[file_name]["is_directory"]

                if is_dir:
                    curr_dir[file_name]["summary"] = msg
                    continue

            # if it is a file
            if "type" in curr_dir[file_name]:

                # check if version isn't already added
                if "version" not in curr_dir[file_name]:
                    continue

                # add it to the list of revisions
                curr_dir[file_name]["revisions"].append(
                    {
                        "version": version,
                        "author": author,
                        "summary": msg,
                        "date": date,
                        "url": curr_dir[file_name]["url"] + "/?p=" + version
                    }
                )
                continue

            # parse file info
            curr_dir[file_name]["author"] = author
            curr_dir[file_name]["date"] = date
            curr_dir[file_name]["version"] = version
            curr_dir[file_name]["summary"] = msg
            curr_dir[file_name]["path"] = path.text
            curr_dir[file_name]["url"] = URL + path.text

            # set file types
            if any(code_end in file_name for code_end in code_ext):
                curr_dir[file_name]["type"] = "Code"
            elif ".txt" in file_name:
                curr_dir[file_name]["type"] = "Text"
            elif ".htm" in file_name:
                curr_dir[file_name]["type"] = "Web Page"
            else:
                curr_dir[file_name]["type"] = "Other"

    return dir


# print(parse_files())
