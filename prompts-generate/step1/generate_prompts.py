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

# 生成所有初始提示和元提示的组合
def generate_prompt_combinations(seed_prompts, meta_prompts):
    combinations = []
    for seed in seed_prompts:
        for meta in meta_prompts:
            prompt = meta.replace('<seed-prompt>', seed)
            combinations.append(prompt)
    return combinations

# 主函数
def main():
    # 从文件中读取初始提示和元提示
    seed_prompts = read_lines_from_file('seed_prompts.txt')
    meta_prompts = read_lines_from_file('meta_prompts.txt')
    
    # 生成初始提示和元提示的组合
    combinations = generate_prompt_combinations(seed_prompts, meta_prompts)
    
    # 将组合保存到输出文件
    write_lines_to_file('output_prompts.txt', combinations)

if __name__ == "__main__":
    main()
