import requests
from bs4 import BeautifulSoup
import os
import json

def scrape_birds():
    # 创建图片存储目录
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    birds_data = {}
    
    # 这里使用百度图片作为示例，实际使用时需要替换为合适的图片源
    birds = [
        {'name': '麻雀', 'search_term': '麻雀 鸟'},
        {'name': '喜鹊', 'search_term': '喜鹊 鸟'},
        {'name': '大山雀', 'search_term': '大山雀 鸟'},
        {'name': '白鹭', 'search_term': '白鹭 鸟'},
        {'name': '乌鸦', 'search_term': '乌鸦 鸟'},
        {'name': '燕子', 'search_term': '家燕 鸟'},
        {'name': '画眉', 'search_term': '画眉鸟'},
        {'name': '鸳鸯', 'search_term': '鸳鸯 鸟'},
        {'name': '斑鸠', 'search_term': '珠颈斑鸠'},
        {'name': '鹦鹉', 'search_term': '虎皮鹦鹉'},
        {'name': '八哥', 'search_term': '八哥鸟'},
        {'name': '百灵鸟', 'search_term': '百灵鸟'},
        {'name': '黄鹂', 'search_term': '黄鹂鸟'},
        {'name': '啄木鸟', 'search_term': '大斑啄木鸟'},
        {'name': '鹰', 'search_term': '普通鵟'},
        {'name': '夜莺', 'search_term': '夜莺 鸟'},
        {'name': '鹌鹑', 'search_term': '鹌鹑 鸟'},
        {'name': '鹧鸪', 'search_term': '鹧鸪 鸟'},
        {'name': '翠鸟', 'search_term': '普通翠鸟'},
        {'name': '戴胜', 'search_term': '戴胜鸟'},
        {'name': '鸽子', 'search_term': '原鸽'},
        {'name': '鹤', 'search_term': '丹顶鹤'},
        {'name': '金翅雀', 'search_term': '金翅雀'},
        {'name': '鹩哥', 'search_term': '鹩哥鸟'},
        {'name': '孔雀', 'search_term': '蓝孔雀'},
        {'name': '鹭鸶', 'search_term': '池鹭'},
        {'name': '猫头鹰', 'search_term': '领角鸮'},
        {'name': '鸨', 'search_term': '大鸨'},
        {'name': '雉鸡', 'search_term': '环颈雉'},
        {'name': '秋沙鸭', 'search_term': '秋沙鸭'},
        {'name': '山雀', 'search_term': '黄腹山雀'},
        {'name': '鹃鸠', 'search_term': '四声杜鹃'},
        {'name': '太平鸟', 'search_term': '太平鸟'},
        {'name': '乌鸫', 'search_term': '乌鸫'},
        {'name': '五色鸟', 'search_term': '五色鸟'},
        {'name': '夜鹰', 'search_term': '普通夜鹰'},
        {'name': '鹬', 'search_term': '青脚鹬'},
        {'name': '鸢', 'search_term': '黑鸢'},
        {'name': '云雀', 'search_term': '云雀'},
        {'name': '伯劳', 'search_term': '棕背伯劳'},
        {'name': '鹪鹩', 'search_term': '鹪鹩'},
        {'name': '鸻', 'search_term': '金眶鸻'},
        {'name': '鸬鹚', 'search_term': '普通鸬鹚'},
        {'name': '鹭', 'search_term': '苍鹭'},
        {'name': '鹮', 'search_term': '朱鹮'},
        {'name': '鹧', 'search_term': '石鹧鸪'},
        {'name': '鹨', 'search_term': '白鹨'},
        {'name': '鹩', 'search_term': '红嘴相思鸟'},
        {'name': '鹑', 'search_term': '黄脚三趾鹑'},
        {'name': '鹕', 'search_term': '白鹈鹕'}
    ]
    
    for bird in birds:
        birds_data[bird['name']] = {
            'images': [],
            'description': get_bird_description(bird['name'])
        }
        
        # 搜索并下载图片
        url = f"https://image.baidu.com/search/index?tn=baiduimage&word={bird['search_term']}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_urls = soup.find_all('img', limit=3)
            
            for i, img in enumerate(img_urls):
                if 'src' in img.attrs:
                    img_url = img['src']
                    img_data = requests.get(img_url, headers=headers).content
                    img_path = f"static/images/{bird['name']}_{i}.jpg"
                    
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                    
                    birds_data[bird['name']]['images'].append(img_path)
                    
        except Exception as e:
            print(f"Error scraping {bird['name']}: {str(e)}")
    
    # 保存鸟类数据到 JSON 文件
    with open('static/birds_data.json', 'w', encoding='utf-8') as f:
        json.dump(birds_data, f, ensure_ascii=False, indent=2)

def get_bird_description(bird_name):
    # 这里可以添加鸟类描述，实际使用时可以从维基百科或其他来源获取
    descriptions = {
        '麻雀': '麻雀是最常见的鸟类之一，体型小巧，善于适应城市环境。',
        '喜鹊': '喜鹊全身黑白相间，叫声清脆，在中国文化中象征着快乐和好运。',
        '大山雀': '大山雀是一种常见的山雀，头部有黑色羽冠，胸部有黄色羽毛。',
        '白鹭': '白鹭全身洁白，常在水边觅食，姿态优美。',
        '乌鸦': '乌鸦全身黑色，智商很高，在许多文化中都有重要象征意义。',
        '燕子': '燕子善于飞行，经常在春季到来时筑巢，被视为带来好运的候鸟。',
        # ... 为其他鸟类添加描述
    }
    return descriptions.get(bird_name, '暂无描述')

if __name__ == '__main__':
    scrape_birds() 