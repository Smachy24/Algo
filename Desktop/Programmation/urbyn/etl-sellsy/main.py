from flask import Flask
import requests
import pandas_gbq as gbq
import pandas as pd
import os

app = Flask(__name__)

URL_BASE="https://api.sellsy.com/v2/"
URL_LOGIN="https://login.sellsy.com/oauth2/access-tokens"
CLIENT_ID="45359340-8022-4d22-bbb7-e41e6d8cd2c1"
CLIENT_SECRET="10a50166e9ea639da4330d9aff92c351819a411d3fe0551362fe892dae5b99ef"

def get_token_sellsy(client,secret):
  data = {"grant_type": "client_credentials","scope":"all","client_id": client, "client_secret": secret}
  response = requests.request("POST", URL_LOGIN, data=data).json()
  return response['access_token']

access_token = get_token_sellsy(CLIENT_ID,CLIENT_SECRET)

def get_all_invoices(token, offset, limit=100):
  """
    Get all invoices informations
    @param token (str): access token
    @param offset (int): invoices'offset
    @param offset (int): invoices'offset
  """
  params = {"limit":limit, "offset":offset}
  headers = {'Authorization':'Bearer '+token}
  response = requests.request("GET", URL_BASE+"invoices",headers=headers, params=params).json()
  return response

def get_all_invoices_id(token, offset):
  """
    Get all invoices'id
    @param token (str): access token
    @param offset (int): invoices'offset
    @return data (list): all invoices'id 
  """
  data = []
  for invoice in get_all_invoices(token, offset)['data']:
    data.append(invoice['id'])
  return data

def get_invoice_data(token, id):
  """
    Get invoice's data
    @param token (str): access token
    @param id (int): invoice's id
    @return data (list): all invoices'id 
  """
  params = {"limit":100}
  headers = {'Authorization':'Bearer '+token}
  data = requests.request("GET", URL_BASE+"invoices/"+str(id),headers=headers,params=params).json() #Une requete get par invoice
  return data

def get_rows_invoice(invoice):
  """
    Get all rows of one invoice
    @param invoice (object) invoice's information
    @return rows_list (list): invoice's rows 
  """
  rows_list= []
  for row in invoice["rows"]:
    rows_list.append(row)  
  return rows_list

def push_gbq(data):
    #Store in big query
    gbq.to_gbq(data,'salto-25b3e.sellsy.invoice_items', project_id='salto-25b3e', if_exists='replace')
    print("Success storing invoices items")

def etl_sellsy():
  """
    Extract, transform and load all invoices
    @param: none
    @return: none
  """
  data = []
  offset = 10000
  offset_max = int(get_all_invoices(access_token,0,5)['pagination']['total'])
  offset_max = (offset_max//100)*100  #Arrondir à la centaine

  while offset <= offset_max:
    for id in get_all_invoices_id(access_token, offset):
      data_invoice = get_invoice_data(access_token,id)
      for row in get_rows_invoice(data_invoice):
        try:
          data.append({"sellsy_invoice_id":id,"sellsy_invoice_number": data_invoice["number"], "sellsy_invoice_amount": data_invoice["amounts"]["total_excl_tax"],
          "sellsy_row_id": row["id"],"sellsy_row_ref": row["reference"],"sellsy_row_pu": row["unit_amount"],"sellsy_row_qty": row["quantity"],
          "sellsy_row_amount": row["amount_tax_exc"], "sellsy_row_description": row["description"] })
        except:
          pass

    offset+=100
  df = pd.DataFrame(data)
  push_gbq(df)
  
@app.route("/")
def main():
  """
    Main function, call etl
    @param: none
    @return (str): function finished 
  """
  etl_sellsy()
  return "etl finished"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))