#Sofia Mase
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Updated sample data for news URLs with topics
# Updated sample data for news URLs with topics
sample_news_data = {
    "Tuition increase": "https://apnews.com/hub/arizona-state-university",
    "Tuition and fee adjustment": "https://students.asu.edu/yourtuition",
    "National Universities Ranking": "https://www.usnews.com/best-colleges/arizona-state-university-1081",
    "QS Ranking": "https://www.topuniversities.com/universities/arizona-state-university",
}

@app.route('/news', methods=['GET'])
def news_focus():
    topics = request.args.getlist('topics[]')

    news_urls = {}

    for topic in topics:
        if topic in sample_news_data:
            news_urls[topic] = sample_news_data[topic]

    return render_template('index.html', news_urls=news_urls)

if __name__ == '__main__':
    app.run(debug=True)
