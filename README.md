# Twitter Scripts

## twitter_list_collector.py

Queries the Twitter API for a Twitter list or file of lists given at the command line and returns a list of usernames. On the assumption that curated lists are a useful signal, we're trying to use this as a discovery tool. At the moment, though, this needs a lot of manual intervention.

### arguments

|  short    |  long           | description                |
|-----------|-----------------|----------------------------|
| -h        | --help          | show help message and exit |
| -u URL    | --url URL       | url of single list         |
| -f FILE   | --file FILE     | file of list URLs          |
| -o OUTPUT | --output OUTPUT | output file                |
