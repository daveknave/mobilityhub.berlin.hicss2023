

# Write Python3 code here
from django.shortcuts import render
import pandas as pd
import json
  
# Create your views here.
def Table(request):
    df = pd.read_csv("rocketman/static/csv/test.csv")
  
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'pandasdata/table.html', context)

