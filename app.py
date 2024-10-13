from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Sample data for baby health, feeding history, and pee/poop counts
sample_health_data = {
    'date': '2024-10-12',
    'baby_weight': '3.5 kg',
    'jaundice_level': '14.9',
    'issues': 'None'
}

sample_feeding_data = [
    {'feed_count': 8, 'date': '2024-10-12'},
    {'feed_count': 7, 'date': '2024-10-11'},
    {'feed_count': 9, 'date': '2024-10-10'},
    {'feed_count': 6, 'date': '2024-10-09'}
]

pee_count = 4
poop_count = 3

# Homepage route
@app.route('/')
def dashboard():
    # Render the dashboard with static sample data
    return render_template('dashboard.html', health_data=sample_health_data, feeding_data=sample_feeding_data, pee_count=pee_count, poop_count=poop_count)

# Feeding history details route
@app.route('/feeding-history')
def feeding_history():
    # Convert sample feeding data to a pandas DataFrame for visualization
    df = pd.DataFrame(sample_feeding_data)
    
    # Get chart type from dropdown (default to line chart)
    chart_type = request.args.get('chart_type', 'line')
    
    # Create the chart based on the selected chart type
    if chart_type == 'line':
        fig = px.line(df, x='date', y='feed_count', title="Feeding History (Line Chart)")
    elif chart_type == 'pie':
        fig = px.pie(df, names='feed_count', title='Feeding Distribution (Pie Chart)')
    else:
        fig = px.histogram(df, x='feed_count', title="Feeding History (Histogram)")
    
    graph = fig.to_html(full_html=False)
    
    return render_template('feeding_history.html', table_data=sample_feeding_data, graph=graph)

# Add similar routes for pee/poop charts or other visualizations as needed...

if __name__ == '__main__':
    app.run(debug=True)
