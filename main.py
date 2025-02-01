import requests
import json

def fetch_quiz_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("quiz", {}).get("questions", []) if isinstance(data, dict) else []
    except requests.exceptions.RequestException as e:
        print(f"\n⚠️ Error fetching data: {e}\n")
        return []

def calculate_accuracy(quiz_results):
    total = len(quiz_results)
    correct = sum(1 for q in quiz_results if q.get("is_correct", False))
    return (correct / total) * 100 if total else 0

def predict_rank_and_college(current_accuracy, historical_accuracy):
    rank = 100000 - int(current_accuracy * 500) - int(historical_accuracy * 400)
    if rank < 10000:
        college = "🏆 Top Tier Medical College"
    elif rank < 50000:
        college = "🎓 Mid Tier Medical College"
    else:
        college = "🏥 Lower Tier Medical College"
    return rank, college

def generate_report():
    print("\n📊 Generating Student Performance Report...\n")
    
    current_quiz = fetch_quiz_data("https://jsonkeeper.com/b/LLQT")
    historical_quiz = fetch_quiz_data("https://jsonkeeper.com/b/XYZ123")
    
    current_accuracy = calculate_accuracy(current_quiz)
    historical_accuracy = calculate_accuracy(historical_quiz)
    predicted_rank, predicted_college = predict_rank_and_college(current_accuracy, historical_accuracy)
    
    report = f"""
    ===============================
        🏅 Student Performance Report 🏅
    ===============================
    📌 Current Accuracy: {current_accuracy:.2f}%
    📌 Historical Accuracy: {historical_accuracy:.2f}%
    
    🎯 Predicted NEET Rank: {predicted_rank:,}
    🎓 Suggested College: {predicted_college}
    ===============================
    """
    return report

print(generate_report())
