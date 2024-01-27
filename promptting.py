
def load_colors(filename):
    """
    Load color data from a text file into a list.
    """
    with open(filename, 'r') as file:
        colors = [line.strip().lower() for line in file.readlines() if line.strip()]
        #剔除空行

    return colors


def list_maching(list1, list2):
    return

##todo: 拆分以下函数为，一个是tags_to_list，一个是tag_review，一个是整体函数
def tags_to_list_to_end(source):
    ##still the copy version of tags

    lines = source.strip().split('\n')
    tag_list = []
    color_list = load_colors(r'D:\0---Program\Projects\Tools\Nai3\NAi-Prompting-Tools\tagbase\colors.txt')
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
        if 'hair' in tag:
            words = tag.split(' ')
            if any(word in color_list for word in words):
                out_tags.append(tag) # Add into out_tags for record
                continue  # Skip this tag as it contains a color word
        # Eye color recognition
        if 'eyes' in tag:
            words = tag.split(' ')
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

        filtered_tags.append(tag)

    return ','.join(filtered_tags), ','.join(out_tags)



#todo: 增加修改逻辑
'''
1.关于头发，发型的识别
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
    color_list = load_colors(color_list_path)
    print(color_list)

    # Formatting the data and printing the result

    # Source data
    source_data = """
    ?
    medium breasts 1.7k
    ?
    6+others 1.7k
    ?
    animal focus 13k
    ?
    architecture 11k
    ?
    armor 171k
    ?
    cape 177k
    ?
    castle 6.4k
    ?
    cloud 241k
    ?
    cloudy sky 60k
    ?
    blue hair 60k
    ?
    blue eyes 60k
    ?
    dragon 18k
    ?
    dragon horns 31k
    ?
    dragon tail 21k
    ?
    fantasy 14k
    ?
    faulds 7.0k
    ?
    full armor 6.0k
    ?
    gauntlets 43k
    ?
    giant 10k
    ?
    giant monster 619
    ?
    gold armor 1.8k
    ?
    helm 2.3k
    ?
    helmet 59k
    ?
    holding 1.0M
    ?
    holding sword 79k
    ?
    holding weapon 196k
    ?
    horns 366k
    ?
    knight 6.1k
    ?
    multiple others 11k
    ?
    outdoors 434k
    ?
    pauldrons 25k
    ?
    plate armor 1.7k
    ?
    shoulder armor 48k
    ?
    sky 353k
    ?
    soldier 3.4k
    ?
    spire 364
    ?
    standing 723k
    ?
    sword 233k
    ?
    tail 624k
    ?
    tower 5.2k
    ?
    weapon 501k
    ?
    wings 361k
    """

    # Formatting the data
    formatted_output,garbage = tags_to_list_to_end(source_data)
    print(formatted_output)
    print('                 ')
    print(garbage or 'No garbage tags found.')