from googleapiclient.discovery import build

my_api_key = "AIzaSyDCPqcGsxho4vtVTsFQlwtI8E8jCRgjHKU"
my_cse_id = "016683987136444378268:kxly9rtf9-e"

def gsearch(string, num):

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']
  
    results = google_search(
        string, my_api_key, my_cse_id, num=10)
    resultlist = []
    print(len(results))
    for x in range(num):
        if x==10:
            break
        resultlist.append(results[x]['link'])
    
    return (resultlist)
