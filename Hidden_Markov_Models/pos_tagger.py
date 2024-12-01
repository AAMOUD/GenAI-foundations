import json
from hmm_model import HiddenMarkovModel  

def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    data_path = "data/tagged_sentences.json"  
    tagged_sentences = load_data(data_path)
    hmm = HiddenMarkovModel()
    hmm.train(tagged_sentences) 
    print("Model trained successfully!")

    test_sentence = ["the", "dog", "barks", "loudly"]
    predicted_tags = hmm.predict(test_sentence)  
    print(f"Sentence: {test_sentence}")
    print(f"Predicted Tags: {predicted_tags}")

if __name__ == "__main__":
    main()
