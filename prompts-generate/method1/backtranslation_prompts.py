from deep_translator import GoogleTranslator
import random
import time

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def write_lines_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

def back_translate(prompts, languages, max_retries=3, sleep_time=2):
    back_translated_prompts = []
    for prompt in prompts:
        for lang in languages:
            retries = 0
            while retries < max_retries:
                try:
                    print(f"Translating prompt: '{prompt}' to {lang}")
                    translated = GoogleTranslator(source='en', target=lang).translate(prompt)
                    time.sleep(sleep_time)  
                    back_translated = GoogleTranslator(source=lang, target='en').translate(translated)
                    back_translated_prompts.append(back_translated)
                    print(f"Back-translated prompt: '{back_translated}'")
                    break  
                except Exception as e:
                    print(f"Translation error for language {lang} on try {retries + 1}: {e}")
                    retries += 1
                    time.sleep(sleep_time * retries)  
    return back_translated_prompts

def main():
    all_prompts = read_lines_from_file('paraphrased_prompts.txt')

    
    high_resource_languages = ['da', 'de', 'it', 'fr', 'nl', 'pt', 'sv', 'es']
    additional_languages = ['no', 'ro', 'ca', 'tr', 'uk', 'pl', 'ru', 'ar']
    
    while len(all_prompts) < 100:
        if len(all_prompts) < 92:
            new_prompts = back_translate(all_prompts, high_resource_languages)
        else:
            new_prompts = back_translate(all_prompts, additional_languages)
        
        all_prompts.extend(new_prompts)
        all_prompts = list(set(all_prompts))  
        print(f"Total prompts: {len(all_prompts)}")
    
    
    write_lines_to_file('expanded_prompts.txt', all_prompts)
    print("Finished writing to file.")

if __name__ == "__main__":
    main()
