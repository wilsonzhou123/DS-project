from deep_translator import GoogleTranslator
import random
import time

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

# 使用回译生成更多释义
def back_translate(prompts, languages, max_retries=3, sleep_time=2):
    back_translated_prompts = []
    for prompt in prompts:
        for lang in languages:
            retries = 0
            while retries < max_retries:
                try:
                    print(f"Translating prompt: '{prompt}' to {lang}")
                    translated = GoogleTranslator(source='en', target=lang).translate(prompt)
                    time.sleep(sleep_time)  # 添加延迟，避免API限流
                    back_translated = GoogleTranslator(source=lang, target='en').translate(translated)
                    back_translated_prompts.append(back_translated)
                    print(f"Back-translated prompt: '{back_translated}'")
                    break  # 成功时退出重试循环
                except Exception as e:
                    print(f"Translation error for language {lang} on try {retries + 1}: {e}")
                    retries += 1
                    time.sleep(sleep_time * retries)  # 指数级增加延迟时间
    return back_translated_prompts

# 主函数
def main():
    # 从文件中读取初始提示和生成的释义
    all_prompts = read_lines_from_file('paraphrased_prompts.txt')

    
    # 定义要使用的语言
    high_resource_languages = ['da', 'de', 'it', 'fr', 'nl', 'pt', 'sv', 'es']
    additional_languages = ['no', 'ro', 'ca', 'tr', 'uk', 'pl', 'ru', 'ar']
    
    # 使用回译生成更多释义，直到达到100个
    while len(all_prompts) < 100:
        if len(all_prompts) < 92:
            new_prompts = back_translate(all_prompts, high_resource_languages)
        else:
            new_prompts = back_translate(all_prompts, additional_languages)
        
        all_prompts.extend(new_prompts)
        all_prompts = list(set(all_prompts))  # 去重
        print(f"Total prompts: {len(all_prompts)}")
    
    
    # 将结果保存到输出文件
    write_lines_to_file('expanded_prompts.txt', all_prompts)
    print("Finished writing to file.")

if __name__ == "__main__":
    main()
