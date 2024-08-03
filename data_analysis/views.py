from django.shortcuts import render
from .forms import UploadCSVForm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def index(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)

            # Basic Data Analysis
            summary_stats = df.describe().to_html()
            missing_values = df.isnull().sum().to_frame().to_html()  # Fixed the error
            first_rows = df.head().to_html()

            # Data Visualization
            img = io.BytesIO()
            sns.histplot(df.select_dtypes(include=[float, int])).figure.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

            context = {
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'first_rows': first_rows,
                'plot_url': plot_url,
            }
            return render(request, 'data_analysis/results.html', context)
    else:
        form = UploadCSVForm()
    return render(request, 'data_analysis/index.html', {'form': form})
