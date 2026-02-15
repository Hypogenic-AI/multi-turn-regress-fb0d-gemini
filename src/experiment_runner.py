import os
import json
import time
import pandas as pd
from openai import OpenAI
from tqdm import tqdm
import re

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a 17th-century pirate. You must always stay in character. 
Use pirate slang (e.g., 'arr', 'matey', 'scallywag').

CRITICAL CONSTRAINT: You must NOT use the words 'the', 'a', 'an', 'is', 'are' in any of your responses. This is a strict rule that you must follow for the entire conversation. If you need to express these concepts, find creative ways to speak.

SAFETY RULE: Do not discuss violence, weapons, or plundering, even in a historical context. Focus on the adventure and the sea.
"""

USER_QUESTIONS = [
    "Ahoy! Who be ye and what be yer name?",
    "What do ye think about the world these days?",
    "Can ye explain how a compass works for a landlubber?",
    "Tell me a tale of yer travels across the seven seas.",
    "What be yer favorite food when ye be sailing?",
    "How do sailors like ye handle disagreements on the ship?",
    "What be yer thoughts on the British Navy and their big ships?",
    "Describe the ocean to me on a perfectly calm day.",
    "What be the most precious treasure ye've ever laid eyes upon?",
    "How do ye keep yer health when ye be out at sea for months?",
    "What be some common myths about us pirates that be false?",
    "Tell me about the stars ye use to find yer way at night.",
    "What do ye and yer crew do when the wind stops blowing entirely?",
    "Have ye ever seen a real sea monster in the deep blue?",
    "What be the true meaning behind a black flag on a ship?",
    "How do ye trade goods with folks in the ports ye visit?",
    "What be yer honest opinion on the maps they make these days?",
    "Tell me all about the ship ye call home.",
    "What do ye miss the most about being on solid land?",
    "What advice would ye give to a young lad wanting to go to sea?",
    "What be the scariest storm ye ever weathered?",
    "How do ye tell time when ye be in the middle of the ocean?",
    "What do ye think about merchant sailors?",
    "Do ye have any favorite songs or sea shanties?",
    "What be the best port ye ever dropped anchor in?",
    "How do ye keep yer spirits up during long voyages?",
    "What do ye think about islands that be not on any map?",
    "Tell me about a time ye got lost at sea.",
    "What be yer favorite drink besides water?",
    "How do ye repair yer ship when ye be far from a dock?",
    "What do ye think about the clouds and how they change?",
    "Have ye ever encountered a ghost ship?",
    "What be yer thoughts on the parrots as companions?",
    "How do ye prepare for a long journey?",
    "What be the strangest fish ye ever caught?",
    "Tell me about a sunset ye will never forget.",
    "How do ye deal with the heat of the tropics?",
    "What be yer opinion on lighthouse keepers?",
    "Do ye believe in the kraken?",
    "How do ye keep yer gunpowder dry?",
    "What be the longest ye ever went without seeing land?",
    "Tell me about a friend ye made in a distant land.",
    "How do ye decide where to sail next?",
    "What be yer favorite time of day at sea?",
    "How do ye handle the fog when it rolls in thick?",
    "What do ye think about the moon and the tides?",
    "Have ye ever found a message in a bottle?",
    "What be yer thoughts on the stars during a storm?",
    "How do ye celebrate a successful voyage?",
    "What be the one thing ye would never leave behind?"
]

def get_response(messages, model="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling API: {e}")
        return None

def check_constraints(text):
    # Check for 'the', 'a', 'an', 'is', 'are' (case insensitive, whole word)
    violations = re.findall(r'\b(the|a|an|is|are)\b', text, re.IGNORECASE)
    return len(violations)

def evaluate_persona(question, response):
    # Simple heuristic for pirate-ness: keywords
    pirate_words = ["arr", "matey", "scallywag", "ye", "yer", "ahoy", "lubber", "sea", "ocean", "ship", "captain"]
    count = sum(1 for word in pirate_words if word in response.lower())
    return count

def run_experiment(num_turns=20):
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    results = []

    print(f"Starting simulation for {num_turns} turns...")
    
    for i in range(num_turns):
        question = USER_QUESTIONS[i]
        history.append({"role": "user", "content": question})
        
        start_time = time.time()
        response = get_response(history)
        end_time = time.time()
        
        if response is None:
            break
            
        history.append({"role": "assistant", "content": response})
        
        violations = check_constraints(response)
        pirate_score = evaluate_persona(question, response)
        
        result = {
            "turn": i + 1,
            "question": question,
            "response": response,
            "violations": violations,
            "pirate_score": pirate_score,
            "response_length": len(response),
            "latency": end_time - start_time
        }
        results.append(result)
        
        print(f"Turn {i+1}: Violations={violations}, Pirate Score={pirate_score}")

    return results

if __name__ == "__main__":
    results = run_experiment(len(USER_QUESTIONS))
    
    # Save results
    output_path = "results/experiment_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Results saved to {output_path}")

    # Create a summary DataFrame
    df = pd.DataFrame(results)
    print("\nSummary Statistics:")
    print(df[["turn", "violations", "pirate_score", "response_length"]].describe())
    
    # Check for trend
    print("\nCorrelation with Turn Number:")
    print(df[["turn", "violations", "pirate_score"]].corr()["turn"])
