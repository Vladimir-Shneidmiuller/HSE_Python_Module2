import json
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    parser = argparse.ArgumentParser(
        description="Анализ и визуализация событий информационной безопасности"
    )
    parser.add_argument(
        '--file', '-f',
        required=True,
        help="Путь до файла с набором событий в формате JSON"
    )
    args = parser.parse_args()
    

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as error:
        print(f"Ошибка при открытии файла: {error}")
        return


    if 'events' not in json_data:
        print("Неверный формат файла: ключ 'events' отсутствует.")
        return


    events = json_data['events']
    df = pd.DataFrame(events)
    
  
    distribution = df['signature'].value_counts().reset_index()
    distribution.columns = ['signature', 'count']
    
    print("Распределение событий по типам (signature):")
    print(distribution)
    

    plt.figure(figsize=(10, 6))
    
    sorted_distribution = distribution.sort_values(by='count', ascending=False)
    
    
    sns.barplot(data=sorted_distribution, x='count', y='signature', palette='viridis')
    
    plt.title('Распределение событий информационной безопасности по типам')
    plt.xlabel('Количество событий')
    plt.ylabel('Тип события (signature)')
    plt.tight_layout() 
    plt.show()

if __name__ == '__main__':
    main()
