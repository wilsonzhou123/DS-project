import random

def read_lines_from_file(filename):
    """从文件中读取行"""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def write_lines_to_file(filename, lines):
    """将行写入文件"""
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

def remove_question_marks(prompts):
    """去除提示符中的问号"""
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

# 主函数
def main():
    # 从文件中读取初始提示
    seed_prompts = read_lines_from_file('seed_prompts.txt')
    paraphrased_prompts = read_lines_from_file('paraphrased_prompts.txt')
    all_prompts = seed_prompts + paraphrased_prompts
    
    # 去除问号
    all_prompts_no_question_marks = remove_question_marks(all_prompts)
    
    # 示例列表
    examples = [
        {"example": "'tough rules for ringtone sellers firms that flout rules on how ringtones and other mobile extras are sold could be cut off from all uk phone networks' is tech."},
        {"example": "'markets signal brazilian recovery the brazilian stock market has risen to a record high as investors display growing confidence in the durability of the country s economic recovery' is business."},
        {"example": "'rock band u2 break ticket record u2 have smashed irish box office records with ticket sales for their dublin concerts after more than 150 000 were sold within 50 minutes' is entertainment."},
        {"example": "'iraq advice claim sparks new row the tories say ministers must respond in parliament to claims that the legal advice used to justify the iraq war was drawn up at number 10' is politics."},
        {"example": "'wales want rugby league training wales could follow england s lead by training with a rugby league club' is sport."}
    ]
    
    # 生成zero-shot提示和few-shot提示
    zero_shot_combinations = generate_prompt_combinations(all_prompts_no_question_marks)
    few_shot_combinations = generate_prompt_combinations(all_prompts_no_question_marks, examples, few_shot=True)
    
    # 将组合与原始提示符一起保存到输出文件
    combined_prompts = all_prompts + zero_shot_combinations + few_shot_combinations
    write_lines_to_file('all_prompts.txt', combined_prompts)

if __name__ == "__main__":
    main()
