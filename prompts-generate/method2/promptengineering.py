import random

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def write_lines_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

def remove_question_marks(prompts):
    return [prompt.replace("?", "") for prompt in prompts]

# Zero-shot prompting example
def zero_shot_classification(prompt):
    complete_prompt = f"{prompt}: business, entertainment, politics, sport or tech?"
    return complete_prompt

# Few-shot prompting with a random example
def few_shot_classification_random_example(prompt, examples):
    example = random.choice(examples)
    example_text = example['example']
    complete_prompt = f"{prompt}: business, entertainment, politics, sport or tech? Example: {example_text}"
    return complete_prompt

# Function to generate prompt combinations
def generate_prompt_combinations(all_prompts, examples=None, few_shot=False):
    combinations = []
    for seed_prompt in all_prompts:
        if few_shot and examples:
            prompt = few_shot_classification_random_example(seed_prompt, examples)
        else:
            prompt = zero_shot_classification(seed_prompt)
        combinations.append(prompt)
    return combinations

def main():
    seed_prompts = read_lines_from_file('seed_prompts.txt')
    paraphrased_prompts = read_lines_from_file('paraphrased_prompts.txt')
    all_prompts = seed_prompts + paraphrased_prompts
    
    all_prompts_no_question_marks = remove_question_marks(all_prompts)
    
    examples = [
        {"example": "'tough rules for ringtone sellers firms that flout rules on how ringtones and other mobile extras are sold could be cut off from all uk phone networks' is tech."},
        {"example": "'markets signal brazilian recovery the brazilian stock market has risen to a record high as investors display growing confidence in the durability of the country s economic recovery' is business."},
        {"example": "'rock band u2 break ticket record u2 have smashed irish box office records with ticket sales for their dublin concerts after more than 150 000 were sold within 50 minutes' is entertainment."},
        {"example": "'iraq advice claim sparks new row the tories say ministers must respond in parliament to claims that the legal advice used to justify the iraq war was drawn up at number 10' is politics."},
        {"example": "'wales want rugby league training wales could follow england s lead by training with a rugby league club' is sport."}
    ]
    
    zero_shot_combinations = generate_prompt_combinations(all_prompts_no_question_marks)
    few_shot_combinations = generate_prompt_combinations(all_prompts_no_question_marks, examples, few_shot=True)
    
    combined_prompts = all_prompts + zero_shot_combinations + few_shot_combinations
    write_lines_to_file('all_prompts.txt', combined_prompts)

if __name__ == "__main__":
    main()
