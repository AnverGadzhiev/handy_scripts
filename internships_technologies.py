def Main() -> None:
    plants = {}
    plants['Yandex'] = ['Go', 'C++', 'Java', 'PHP', 'Python']
    plants['Tinkoff'] = ['Go', 'C++', 'Scala', 'Java', 'Python', '.NET']
    plants['Sberbank'] = ['Go', 'C++', 'Python', 'Java']
    plants['Ozon'] = ['Go', '.NET', 'Java'] 
    
    print(*GetTechnologiesIntersection(plants))
    

def GetTechnologiesIntersection( plants : dict[str, list[str]]) -> set[str]:
    common_technologies = set(next(iter(plants.values())))
    for _, technologies_list in plants.items():
        common_technologies = set(technologies_list).intersection(common_technologies)
    return common_technologies

if __name__ == '__main__':
    Main()