def earliest_ancestor(ancestors, starting_node):
    ancestors_list = []
    oldest_ancestor = None
    oldest_generation = 0

    def helper(ancestors, starting_node, generations):
        # obtain a list of all nodes used 
        cache = set()
        for pair in ancestors:
            if starting_node == pair[1] and starting_node not in cache:
                cache.add(pair[0])

        if len(cache) > 0:
            for parent in cache:
                node = (helper(ancestors, parent, generations+1))
                if node != None:
                    ancestors_list.append(node)
        else:
            return (starting_node, generations)
    
    helper(ancestors, starting_node, 0)
    print(f"Starting node is: {starting_node}")
    print(f"[(ancestor, generation)]: {ancestors_list}")
    print()
    for ancestor in ancestors_list:
        if ancestor[1] > oldest_generation:
            oldest_ancestor = ancestor
            oldest_generation = ancestor[1]
        elif ancestor[1] == oldest_generation:
            if ancestor[0] < oldest_ancestor[0]:
                oldest_ancestor = ancestor
                oldest_generation = ancestor[1]
    
    if oldest_ancestor != None:
        return oldest_ancestor[0]
    else:
        return -1

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    earliest_ancestor(test_ancestors, 6)