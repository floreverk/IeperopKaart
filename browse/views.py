import pandas as pd
from django.conf import settings
import os
from django.shortcuts import render

def kaart_view(request):
    excel_path = os.path.join(settings.BASE_DIR, 'static/data/markers.xlsx')
    df = pd.read_excel(excel_path)

    markers = []
    for _, row in df.iterrows():
        markers.append({
            'titel': row['titel'],
            'lat': row['lat'],
            'lon': row['lon'],
            'tekst': row['tekst'],
            'afbeelding': f"/static/markers/{row['bestandsnaam']}"
        })

    return render(request, 'kaart.html', {'markers': markers})


