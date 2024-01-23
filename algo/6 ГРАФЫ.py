# ГРАФЫ поиск в ширину
def person_is_seller(name):
    name[-1] == "m"

from collections import deque # поключили библиотеку для очереди
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):  # поиск в ширину  по графам
    search_queue = deque()                     # создали очередь
    search_queue += graph["you"]               # добавили всех соседий в очередь поиска
    searched = []                              # Массив для уже проверенных людей
    while search_queue:                        # Пока очередь не пуста
        person = search_queue.popleft()        # Из очереди достаем первый элемент
        if not person in searched:             # проверяется если нет в списке проверенных
            if person_is_seller(person):       # проверяем соответствует ли поиску
                print(person + "нужный человек")
                return True
            else:
                search_queue += graph[person]  # если не соответствует поиску проверяем всех его друзей
                searched.append(person)        # человек помечанный как уже проверянный
    return False                               # в очереди нет искомого


# ГРАФЫ Алгоритм Дейкстры
graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['fin'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['fin'] = infinity

parenst = {}
parenst['A'] = 'start'
parenst['B'] = 'start'
parenst['fin'] = None

processed = []

def find_lowest_cost_node(costs):               # определяет узел с наименьшей стоимостью
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:                          # перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если узел с наименьшей стоимостью из уже виденных и небыл обработан
            lowest_cost = cost                            # он назначается узлом с наменьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)             # определяет узел с наименьшей стоимостью
while node is not None:                         # пока не обработанны все узлы
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():                  # перебрать всех соседий тикущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:                 # если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost                 # обновить стоимость этого узла
            parenst[n] = node                   # это узел становиться новым родителем для соседа
    processed.append(node)                      # узел помечается как обработанный
    node = find_lowest_cost_node(costs)         # найти следующий узел и повторить