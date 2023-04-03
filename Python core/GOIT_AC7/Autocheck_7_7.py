def data_preparation(list_data):
    join_data =[]
    for list in list_data:
        if len(list)>2:
            list.remove(max(list))
            list.remove(min(list))
        join_data.extend(list)
    join_data.sort(reverse=True)
    return join_data