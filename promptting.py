
def load_matching_list(filename):
    """
    Load base data from a text file into a list.
    """
    with open(filename, 'r') as file:
        lists = [line.strip().lower() for line in file.readlines() if line.strip()]

        #剔除空行

    return lists


def list_maching(list1, list2):
    return

##todo: 拆分以下函数为，一个是tags_to_list，一个是tag_review，一个是整体函数
def tags_to_list_to_end(source):
    ##still the copy version of tags

    lines = source.strip().split('\n')
    tag_list = []
    color_list = load_matching_list(r'D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\colors.txt')
    hair_style_list = load_matching_list(r'D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\hair_style.txt')
    redundant_list = ['breasts']
    kill_list = []

    for line in lines:
        # Filtering out empty lines and lines with only a question mark
        if line.strip() and not line.strip() == '?':
            # Extracting the phrase part (before the number), if present
            parts = line.split(' ')
            if len(parts) > 1:
                phrase = ' '.join(parts[:-1]).replace('?', '').strip()
                tag_list.append(phrase)

    filtered_tags = []
    out_tags = []

    for tag in tag_list:
        # Hair color and style recognition
        words = tag.split(' ')
        if 'hair' in words: # If the tag contains the word 'hair' instead of have 'hair' as part of a word
            if any(word in color_list for word in words):
                out_tags.append(tag) # Add into out_tags for record
                continue  # Skip this tag as it contains a color word
        # Eye color recognition
        if 'eyes' in tag:
            if any(word in color_list for word in words):
                out_tags.append(tag)  # Add into out_tags for record
                continue
        # Redundant tag removal
        if any(kill_word in tag for kill_word in kill_list):
            out_tags.append(tag)  # Add into out_tags for record
            continue  # Skip this tag as it is redundant
        if tag in redundant_list:
            out_tags.append(tag)  # Add into out_tags for record
            continue  # Skip this tag as it is redundant
        if tag in hair_style_list:
            out_tags.append(tag)  # Add into out_tags for record
            continue  # Skip this tag as it is redundant

        filtered_tags.append(tag)

    return ','.join(filtered_tags), ','.join(out_tags)



#todo: 增加修改逻辑
'''
1.关于头发，发型的识别 完成
2.关于冗余词汇的识别
2.0 纯净模式，连1girl与其他基本外貌特征一律不要，方便衔接在人设后
2.1 breast - 替换为medium breasts，如果有则直接删除（设立一个flag来确定之前有没有添加。顺序也可以用flag的方法来判别：1girl，breasts，hair，eyes。。。）
    每个flag带有一个顺序占位器与一个计数器，继续器如果是0，则按照固定的规则，通过别的flag的占位器来判断插入的顺序
2.2
3.特殊特征，兽耳，兽尾，翅膀，尾巴，角，

'''

if __name__ == '__main__':
    #absolut path D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\colors.txt
    color_list_path = r'D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\colors.txt'
    color_list = load_matching_list(color_list_path)
    hair_style_list_path = r'D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\hair_style.txt'
    hair_style_list = load_matching_list(hair_style_list_path)
    print(hair_style_list)
    print(color_list)

    # Formatting the data and printing the result

    # Source data
    source_data = """
    
?
1girl 5.1M

?
animal ears 938k

?
blue gloves 18k

?
blue hairband 13k

?
blush 2.5M

?
braid 520k

?
brown hair 1.3M

?
clenched hand 46k

?
closed mouth 861k

?
collarbone 649k

?
ear ribbon 3.8k

?
fingerless gloves 213k

?
gloves 1.1M

?
green ribbon 18k

?
hair ornament 1.2M

?
hairband 394k

?
hairclip 278k

?
horse ears 83k

?
horse girl 74k

?
horse tail 47k

?
looking at viewer 2.7M

?
midriff 256k

?
multicolored hair 492k

?
navel 965k

?
official alternate costume 221k

?
ribbon 929k

?
short hair 1.9M

?
short sleeves 494k

?
simple background 1.4M

?
skirt 1.3M

?
smile 2.3M

?
solo 4.2M

?
star (symbol) 191k

?
star hair ornament 24k

?
streaked hair 170k

?
tail 626k

?
white background 1.1M

?
white hair 556k

?
yellow eyes 558k
    """

    # Formatting the data
    formatted_output,garbage = tags_to_list_to_end(source_data)
    print(formatted_output)
    print('                 ')
    print(garbage or 'No garbage tags found.')