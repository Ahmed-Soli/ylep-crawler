import requests , os , csv
from urllib.parse import urljoin

def SaveAsCsv(list_of_rows):
  try:
    with open('data.csv', mode='a',  newline='', encoding='utf-8') as outfile:
      csv.writer(outfile).writerow(list_of_rows)
  except PermissionError:
    print("Please make sure data.csv is closed\n")


def Search():
  payload = {
        'find_desc': 'Restaurants',
        'find_loc': 'Nashville, TN',
        'start': 30, #if you want second page set start to 60 and so on
        'parent_request_id': 'f3d6966567be99d1',
        'request_origin': 'user'}
  res = requests.get(url, params=payload)
  if res.status_code == 200:
    return res.json()

def Extract():
  try:
    JsonObj          = Search()
    Data             = JsonObj['searchPageProps']['searchResultsProps']['searchResults']
    if Data is not None:
      for index , item in enumerate(Data,1):
        print('getting item {} out of {}'.format(index,len(Data)))
        if item.get('searchResultBusiness','') :
          name   = item['searchResultBusiness']['name']
          rating = item['searchResultBusiness']['rating']
          price  = item['searchResultBusiness']['priceRange']
          rank   = item['searchResultBusiness']['ranking']
          review = item['searchResultBusiness']['reviewCount']
          phone  = item['searchResultBusiness']['phone']
          busUrl = urljoin(url ,item['searchResultBusiness']['businessUrl'])
          SaveAsCsv([name,rating,price,rank,review,phone,busUrl])
  except Exception as e:
    print(e)

  
url = 'https://www.yelp.com/search/snippet'
if os.path.isfile('data.csv') and os.access('data.csv', os.R_OK):
  print("File data.csv Already exists \n")
else:
  SaveAsCsv([ 'name','rating','priceRange','ranking','reviewCount','phone','businessUrl'])
Extract()
