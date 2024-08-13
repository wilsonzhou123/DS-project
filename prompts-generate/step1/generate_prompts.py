def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def write_lines_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

def generate_prompt_combinations(seed_prompts, meta_prompts):
    combinations = []
    for seed in seed_prompts:
        for meta in meta_prompts:
            prompt = meta.replace('<seed-prompt>', seed)
            combinations.append(prompt)
    return combinations

def main():
    seed_prompts = read_lines_from_file('seed_prompts.txt')
    meta_prompts = read_lines_from_file('meta_prompts.txt')
    
    combinations = generate_prompt_combinations(seed_prompts, meta_prompts)
    
    write_lines_to_file('output_prompts.txt', combinations)

if __name__ == "__main__":
    main()
